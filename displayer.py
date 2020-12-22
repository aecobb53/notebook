import argparse
import logging
import libtmux
import os

# https://libtmux.git-pull.com/api.html

working_directory = os.environ['HOME'] + f'/notebook/'

# Logging
logit = logging.getLogger('TaskWarrior')
logit.setLevel(logging.DEBUG)
log_file = working_directory + 'logs/tmux_logging.log'
fh = logging.FileHandler(log_file)
ch = logging.StreamHandler()
fh.setLevel(logging.DEBUG)
ch.setLevel(logging.WARN)

# Argparse
aparse = argparse.ArgumentParser(description='Task Warrior TMUX wrapper')
aparse.add_argument('--attatch', action='store_false', help='Dont attatch the process')
aparse.add_argument('--exit', action='store_false', help='Dont kill the process at exit')
aparse.add_argument('-p', action='append', help='Project flag')
aparse.add_argument('-t', action='append', help='Tag flag')
aparse.add_argument('-pri', action='append', help='Priority above/below')
aparse.add_argument('-set', action='append', help='Pre set displays')
aparse.add_argument('-kill', action='store_false', help='Find and close session with matching name')
aparse.add_argument('--killall', action='store_true', help='Find and close ALL sessions with matching name')

args = aparse.parse_args()
# print(args)

logit.info(f"args:{args}")

def _update_name(session_name, count = 0):
    session_name = list(session_name)
    while True:
        try:
            int(session_name[-1])
        except ValueError:
            session_name.append(str(count))
            return ''.join(session_name), count
        else:
            session_name.pop(-1)
            count += 1


class Command:

    def __init__(self):
        self.projects = []
        self.tags = []
        self.priorities = []
        self.status = []
        self.cmd = ''
        self.empty = True

    """project"""
    def andproject(self, project):
        self.empty = False
        if self.projects == []:
            self.projects.append(f"project:{project}")
        else:
            self.projects.append(f"and project:{project}")

    def orproject(self, project):
        self.empty = False
        if self.projects == []:
            self.projects.append(f"project:{project}")
        else:
            self.projects.append(f"or project:{project}")

    def noproject(self, project):
        self.empty = False
        self.projects = ['project:']


    """tag"""
    def andtag(self, tag):
        self.empty = False
        if self.tags == []:
            self.tags.append(f"+{tag}")
        else:
            self.tags.append(f"+{tag}")

    def ortag(self, tag):
        self.empty = False
        if self.tags == []:
            self.tags.append(f"+{tag}")
        else:
            self.tags.append(f"or +{tag}")

    def nottag(self, tag):
        self.empty = False
        if self.tags == []:
            self.tags.append(f"-{tag}")
        else:
            self.tags.append(f"-{tag}")

    def notag(self, tag):
        self.empty = False
        self.tags = ['tag:']


    """priority"""
    def andpriority(self, priority):
        self.empty = False
        priority = priority.upper()
        if priority not in ['H', 'M']:
            raise ValueError('Not a valid priority')
        if self.priorities == []:
            self.priorities.append(f"priority:{priority}")
        else:
            self.priorities.append(f"and priority:{priority}")

    def orpriority(self, priority):
        self.empty = False
        priority = priority.upper()
        if priority not in ['H', 'M']:
            raise ValueError('Not a valid priority')
        if self.priorities == []:
            self.priorities.append(f"priority:{priority}")
        else:
            self.priorities.append(f"or priority:{priority}")

    def nopriority(self, priority):
        self.empty = False
        self.priorities = ['priority:']


    """status"""
    def andstatus(self, status):
        self.empty = False
        if status not in ['pending', 'complete', 'deleted']:
            raise ValueError('Not a valid priority')
        if self.status == []:
            self.status.append(f"status:{status}")
        else:
            self.status.append(f"and status:{status}")

    def orstatus(self, status):
        self.empty = False
        if status not in ['pending', 'complete', 'deleted']:
            raise ValueError('Not a valid priority')
        if self.status == []:
            self.status.append(f"projestatusct:{status}")
        else:
            self.status.append(f"or prostatusject:{status}")

    def nostatus(self, status):
        self.empty = False
        self.status = ["status:"]

    def set_cmd(self):
        cmd_lst = [
            f'sh {working_directory}sim_watch.sh "', 
            'task',
        ] + \
        self.projects + \
        self.tags + \
        self.priorities + \
        self.status + \
        ['"']
        if self.empty:
            self.cmd = ''
            return self.cmd
        else:
            new_cmd = ' '.join(cmd_lst)
            self.cmd = ''.join(new_cmd)
            self.cmd
        return self.cmd


class TaskWarriorTmux:

    def __init__(self, session_name):
        self.orig_session_name = session_name
        self.session_name = self.orig_session_name
        self.cmd_lst = [[Command()]]
        self.cmd = [0, 0]

        self.server = libtmux.Server()
        self.create_session()
        self.select_window(0).select_pane(0)

    def create_session(self, session_name=None):
        if session_name == None:
            session_name = self.session_name
        count = 0
        while True:
            try:
                session = self.server.new_session(session_name)
                break
            except libtmux.exc.TmuxSessionExists:
                session_name, count = _update_name(session_name, count)
        self.session = session
        self.session_name = session_name
        return self.session

    def create_window(self, new_window_name=''):
        self.window = self.session.new_window()
        self.cmd_lst.append([Command()])
        return self.window

    def split_window(self, vert_bool=True):
        self.pane = self.window.split_window(vertical=vert_bool,attach=True)
        self.cmd_lst[self.cmd[0]].append([Command()])
        return self.pane

    def add_cmd(self):
        self.cmd_lst[self.cmd[0]].append(Command())

    def select_window(self, number):
        self.window = self.session.select_window(number)
        self.cmd[0] = number
        return self.window

    def select_pane(self, number):
        if number <0:
            print(number)
            print(len(self.window.list_panes()))
            print(self.window.list_panes())
            for i in self.window.list_panes():
                print(i)
        self.pane = self.window.select_pane(number)
        self.cmd[1] = number
        return self.pane

    def create_grid(self, x=1, y=1):
        """Create the rows"""
        for j in range(y-1):
            self.window.cmd('split-window', '-v')
            self.add_cmd()
        """Create the columns"""
        for j in range(y):
            pane_number = j * x
            self.window.cmd('select-pane', '-t', str(pane_number))
            for i in range(x-1):
                self.window.cmd('split-window', '-h')
                self.add_cmd()
        """Itterate through and resize"""
        rows, columns = os.popen('stty size', 'r').read().split()
        pane_x = int(columns)
        pane_y = int(rows)
        for p in range(x * y):
            # If we are on the right or bottom edge we dont want to re-size the dimentions of the pane
            if (p+1) % x == 0:
                right_side = False
            else:
                right_side = True
            if p >= x*y-x:
                bottom_side = False
            else:
                bottom_side = True

            self.window.cmd('select-pane', '-t', str(p))
            if right_side:
                self.window.cmd('resize-pane', '-x', str(pane_x // x))
            if bottom_side:
                self.window.cmd('resize-pane', '-y', str(pane_y // y))

    def resize_pane(self, pane, horz, vert):
        self.select_pane(pane)
        if vert > 0: 
            self.pane.resize_pane(height=vert)
        if horz > 0:
            self.pane.resize_pane(width=horz)

    def close_pane(self, pane):
        self.select_pane(pane)
        self.cmd_lst[self.cmd[0]].pop(pane)
        self.pane.cmd('kill-pane')

    def set_cmds(self):
        for el in self.cmd_lst[self.cmd[0]]:
            el.set_cmd()

    def run_cmds(self, max_index, sendit=True):
        self.set_cmds()
        for index, pane in enumerate(self.window.list_panes()):
            self.select_pane(index)
            self.pane.send_keys(f'{self.cmd_lst[self.cmd[0]][index].cmd}', enter=sendit)
            if index >= max_index:
                break

    def attach(self):
        self.session.attach_session()

    def exit(self):
        self.session.kill_session()
        # try:
        #     self.session.kill_session()
        # except libtmux.exc.LibTmuxException:
        #     pass

    def purge_sessions(self):
        logit.info(f'killing all sessions matching {self.orig_session_name}')
        server = libtmux.Server()
        try:
            for session in server.list_sessions():
                print(f"session stuff: {str(session)}")
                print(self.session_name, str(session))
                if self.orig_session_name in str(session):
                    print(f"Killing session: {session}")
                    logit.debug(f"Killing session: {session}")
                    session.kill_session()
        except libtmux.exc.LibTmuxException:
            print('No sessions to close... exiting')
            logit.debug('No sessions to close... exiting')

    def smart_grid(self):
        #based on the cmds for the window, set the panes up
        pass

    def select_cmd_index(self, index):
        self.cmd_index = index

        



tnt = TaskWarriorTmux('TaskWarrior')

rows, columns = os.popen('stty size', 'r').read().split()
window_x = int(columns)
window_y = int(rows)
if window_x <= 200:
    grid_x, grid_y = 2,2
    tnt.create_grid(grid_x, grid_y)
    tnt.resize_pane(2,window_x/grid_x,5)
    tnt.close_pane(3)
    max_cmd_index = 1
elif window_x > 200:
    grid_x, grid_y = 3,2
    tnt.create_grid(grid_x, grid_y)
    tnt.resize_pane(3,window_x/grid_x,5)
    tnt.close_pane(4)
    tnt.close_pane(4)
    max_cmd_index = 2
else:
    grid_x, grid_y = 1, 1
    tnt.create_grid(grid_x, grid_y)
    tnt.resize_pane(1,window_x/grid_x,5)
    max_cmd_index = 1



# tnt.create_window()
window_cnt = 0



if not any([True for i in [args.p, args.t, args.pri, args.set] if i != None]):
    args.set = ['0']

if args.set[0] == '0':
    
    # Pane 0
    pane = 0
    tnt.cmd_lst[window_cnt][pane].orpriority('H')
    tnt.cmd_lst[window_cnt][pane].orpriority('M')

    # Pane 1
    pane = 1
    tnt.cmd_lst[window_cnt][pane].nottag('code')
    tnt.cmd_lst[window_cnt][pane].nottag('learn')

    # Pane 2
    pane = 2
    tnt.cmd_lst[window_cnt][pane].ortag('learn')
    tnt.cmd_lst[window_cnt][pane].ortag('code')

    # # Pane 3
    # pane = 3
    # tnt.cmd_lst[window_cnt][pane].mark_empty()

    # # Pane 4
    # pane = 4
    # tnt.cmd_lst[window_cnt][pane].mark_empty()
    # tnt.select_pane(1)

# tnt.set_cmds()
tnt.run_cmds(max_cmd_index)
tnt.select_pane(3)

# for index, c in enumerate(tnt.cmd_lst[0]):
#     print(c.__dict__)
#     print(c.cmd)

# for index, pane in enumerate(tnt.window.list_panes()):
#     pane.send_keys(f'{tnt.cmd_lst[tnt.cmd[0]][index].cmd}', enter=False)
    
if args.killall:
    tnt.purge_sessions()
    exit()

print(args)
if args.attatch:
    tnt.attach()
if args.exit:
    tnt.exit()
exit()

