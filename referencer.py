import argparse
import os
import re
import json
import yaml
from etc import string_colors
from etc import conf_manager

"""
set the env variable NOTEBOOK  to /home/acobb/notebook 
"""

# Configs
"""
There are three configs of note
- etc/referencer.yml file is for notes and tmux windows
- etc/default_notebookrc.yml for default rc file details
- $HOME/.notebookrc for user updated rc file values
"""

main_dir = os.getenv('NOTEBOOK')
master_config_path = main_dir + '/' + 'etc/referencer.yml'
master_rc_path = main_dir + '/' + 'etc/default_notebookrc.yml'
config = {}
rc_file = {}

# Main config
with open(master_config_path) as ycf:
    master_config = yaml.load(ycf, Loader=yaml.FullLoader)
config.update(master_config)
# Default RC
with open(master_rc_path) as ycf:
    master_rc = yaml.load(ycf, Loader=yaml.FullLoader)


# User RC
def update_rc(orig, new):
    newdct = orig
    for key, value in new.items():
        print(key, value)
        if key not in newdct:
            newdct[key] = []
        for val in value:
            if val.endswith('/n'):
                for dex, item in enumerate(newdct[key]):
                    if val[:-2] == item:
                        newdct[key].remove(item)
                        break
            else:
                newdct[key].append(val)
    return newdct

# Load personal rc file
with open(master_rc['rc_file']) as ycf:
    new_rc_updates = yaml.load(ycf, Loader=yaml.FullLoader)

print(json.dumps(master_rc, indent=2))
print(json.dumps(new_rc_updates, indent=2))

# Update the rc file
rc_file['color_module'] = master_rc['color_module']
rc_file = update_rc(rc_file, master_rc['notes'])
rc_file = update_rc(rc_file, master_rc['colors'])
try:
    rc_file = update_rc(rc_file, new_rc_updates['notes'])
except:
    pass

try:
    rc_file = update_rc(rc_file, new_rc_updates['colors'])
except:
    pass

try:
    rc_file['color_module'] = new_rc_updates['color_module']
except:
    pass

print(json.dumps(rc_file, indent=4))

# Colors
exec('SC = string_colors.Bit' + str(rc_file['color_module']) + '()')
# exec('SC = string_colors.Bit' + str(master_rc['color_module']) + '()')
print(SC.clc) # To clear any syntax added before this script runs.

# Set colors here:
for element, colors in master_rc['colors'].items():
    """
    For each color in the rc files this function tries to assign the color name to a SC argument.
    If it cant it tires to append the exact string.
    By default this assigns:
    FILE HEADER GREP BLOCK TABLE1 TABLE2 NOTE
    """
    exec(element + " = ''")
    for color in colors:
        try:
            exec(element + " += SC." + color)
        except SyntaxError:
            exec(element + " += '" + color + "'")
        except AttributeError:
            exec(element + " += '" + color + "'")
    # print(exec(element))


## ARGPARSE
# Creating parser
parser = argparse.ArgumentParser(prog='referencer', description='display markdown notes easier')

# Adding arguments
parser.add_argument('-G','-g', '--grep',      action='count',       help='grep level: grep / grep -C10 / entire file / any number highter results in a list of files')
parser.add_argument('-D','-d', '--directory', action='append',      help='specify a directory')
parser.add_argument('-E','-e', '--extended',  action='append',      help='extended directory search')
parser.add_argument('-A','-a', '--AND',       action='append',      help='AND operation')
parser.add_argument('-O','-o', '--OR',        action='append',      help='OR operation')
parser.add_argument('-N','-n', '--NOT',       action='append',      help='NOT operation')
parser.add_argument('-L','-l', '--list',      action='append',      help='Search in order provided')
parser.add_argument('-C','-c', '--color',     action='store_false', help='Turn output color and markdown reader off')
parser.add_argument('-S','-s', '--sensitive', action='store_true',  help='Search sensative to case')
parser.add_argument('-R','-r', '--recursive', action='store_false', help='Recursive search down directories')
parser.add_argument('--nonmarkdown',          action='store_true',  help='Look is more than just markdown files')
parser.add_argument('--config',               action='store_true',  help='For info, run --config help')
parser.add_argument('search', nargs='*')

# Setting markdown flag
md = False

# Parsing arguments
args = parser.parse_args()

# These values dont seem to save properly in yaml, i will look into it eventually but for now they are just added here
config['regex_strings'] = {}
config['regex_strings']['header_s'] = "^ *?##* .*"
config['regex_strings']['break_s'] = "^ *(----*|\*\*\*\**|____*) *$"
config['regex_strings']['note_s'] = "^ *>>*"
config['regex_strings']['line_s'] = ".*\!?[.*\]\(.*\)"
config['regex_strings']['hidden_start_s'] = "^ {0,3}\[//\]: # \(.*"
config['regex_strings']['hidden_end_s'] = "\)"
config['regex_strings']['html_cmd_start_s'] = "<!--"
config['regex_strings']['html_cmd_end_s'] = "-->"

if args.directory == None and args.extended == None:
    directory = [master_rc['default_dir']]
else:
    if args.extended:
        directory = args.extended + [rc_file['default_dir']]
    else:
        directory = args.directory


# Config
if args.config:
    # print('running config\n\n')
    home = os.getenv('HOME')
    rf_file_path = home + '/' + config['rc_filename']
    new_config = {}
    new_config_file = []
    accepted_config_keys = [
        'default_dir',
        'color_module',
        'default_files',
        'ignore_files',
        'other_dir',
        'html_cmds',
        'colors',
    ]
    if not os.path.exists(rf_file_path):
        print(f'Creating rc file {rf_file_path}')
        os.mknod(rf_file_path)
    if 'help' in args.search:
        one = '\t'
        two = '\t\t'
        print('running config help:\n\n')
        # key/value pairs
        print('The key/value pairs:')
        print(one + 'Key value pair defaults are overwritten by whatever you add.')

        print(one + 'default_dir:')
        print(two + 'Default directory points to wherever your current install of notebook is')
        print(two + 'Example: notes --config default_dir /home/USERNAME/git/notebook')

        print(one + 'color_module:')
        print(two + 'Sets the color bit type (256 is default but you can also select 16, or 8)')
        print(two + 'Example: notes --config color_module 16')
        print('\n')

        # note specific lists
        print('The note specific lists')
        print(one + 'Lists can be appended or items removed. The removal explanation is after this.')

        print(one + 'default_files')
        print(two + 'Adds to the list of files that the parser looks through. All other file types are ignored by the parser. The default type is .md')
        print(two + 'Example: notes --config default_files .txt')

        print(one + 'ignore_files')
        print(two + 'Adds to the list of files that are ignored. By default the only one is README.md')
        print(two + 'Example: notes --config ignore_files README_ignore.md')

        print(one + 'other_dir:')
        print(two + 'other directory adds to the list of default directories used. Remember notes searches recursivly by default.')
        print(two + 'Example: notes --config default_dir /home/USERNAME/git/notebook')
        print('')

        # Removing items
        print('Any config value can be removed by adding "not" before the key. If it is a default config value it will appear in your rc config to overrite the values')
        print(one + 'Example notes --config not ignore_files README_ignore.md')

        # Setting colors
        print('Adding colors to notes')
        print(one + 'Colors can be selected from all available colors in the color_module. You set what they are called and what they do so two arguments are needed.')

        print(one + 'html_cmds:')
        print(two + 'If you want colors in the text of markdown files you can add colors to html comments. An example would be <!-- red --> something in red <!-- clc -->. The red sets the color and the clc clears it. Because each command needs a name and what it does there are two arguments for the colors. This is a list so multiple colors or formats can be added to the same command. The list of available colors is quite extensive so run notes --config colors pallet for a list.')
        print(two + 'Example: notes --config html_cmds red red')
        print(two + 'Example: notes --config html_cmds warning bright_red background_white blinking')

        print(one + 'colors:')
        print(two + 'Colors differ from html_cmds because they are used in the code itself. Filenames have different colors from the headers so you can change those with colors. ')
        print(two + 'Example: notes --config colors FILE bright_red')
        print(two + 'Example: notes --config colors table red back_green italic')
        exit()

    if args.search == ['colors', 'pallet']:
        print('Currently available colors. The left column is how it looks and the right is how to call it. All calls are SC.<color>\n\n')
        SC.print_pallet()

    if not isinstance(args.search, list) or len(args.search) < 2:
        print('Not enough arguments to update the config')
        exit()


    # print(args.search)
    # print(type(args.search))
    # print(json.dumps(new_config,indent=2))

    try:
        with open(rf_file_path) as ycf:
            old_conf = yaml.load(ycf, Loader=yaml.FullLoader)
            # new_config.update(yaml.load(ycf, Loader=yaml.FullLoader))
        for key, value in old_conf.items():
            if key in ['notes']:
                for k, v in value.items():
                    new_config.update({k:v})
            else:
                new_config.update({key: value})
    except:
        pass


    # deletename = 'colors'
    # if deletename in new_config.keys():
    #     del new_config[deletename]

    # print(json.dumps(new_config,indent=4))


    def key_value(key, value, validate=None):
        print(key + ': ' + value)
        
        if key not in accepted_config_keys:
            print('not a key')
            return False
        
        if validate != None:
            if value not in validate:
                print('not a valid value')
                return False
        
        try:
            value = int(value)
        except:
            pass
        
        new_config[key] = value

    def list_items(key, value, validate=None):
        print(key + ': ' + value)

        if key not in accepted_config_keys:
            print('not a key')
            return False
        
        if key not in new_config.keys():
            new_config[key] = []
        
        if validate != None:
            if value not in validate:
                print('not a valid value')
                return False

        if value in new_config[key]:
            return False
    
        try:
            value = int(value)
        except:
            pass
        new_config[key].append(value)

    def update_colors(category, key, values, validate=None):
        if not isinstance(values, list):
            values = [values]
        print(category + ':  ' + key + ': ' + str(values))

        if category not in accepted_config_keys:
            print('not a key')
            return False
        
        if category not in new_config.keys():
            new_config[category] = {}

        if key not in new_config[category].keys():
            new_config[category][key] = []
        
        for value in values:
            skip = False
            if validate != None:
                if value not in validate:
                    print('not a valid value')
                    skip = True

            if value in new_config[category][key]:
                skip = True

            if skip:
                return False
        
            try:
                value = int(value)
            except:
                pass
        
            new_config[category][key].append(value)


    if args.search[0] == 'default_dir':
        key_value(args.search[0], args.search[1])

    if args.search[0] == 'color_module':
        key_value(args.search[0], args.search[1], ['256', '16', '8'])


    if args.search[0] == 'default_files':
        list_items(args.search[0], args.search[1])

    if args.search[0] == 'ignore_files':
        list_items(args.search[0], args.search[1])

    if args.search[0] == 'other_dir':
        list_items(args.search[0], args.search[1])


    if args.search[0] == 'html_cmds':
        update_colors('html_cmds', args.search[1], args.search[2:])

    if args.search[0] == 'colors':
        update_colors('colors', args.search[1], args.search[2:])

    # Dont use yaml write so you can add notes colors and other headers to the lists

    ### it seems to be deleting the list items for unknown reasons

    indent = "    "

    # print(json.dumps(new_config,indent=4))

    # new_config = {}
    # new_config['default_dir'] = '/home'
    # new_config['color_module'] = 256
    # new_config['default_files'] = ['.md', '.txt']
    # new_config['ignore_files'] = ['.txt']
    # new_config['other_dir'] = ['/home/acobb/git', '/home']
    # # new_config['other_dir'] = ['/home/acobb/git']
    # new_config['html_cmds'] = {'blue': ['blue']}
    # new_config['colors'] = {'FILE': ['red', 'back_white', 'italic'], 'white': ['grey', 'italic']}

    if 'default_dir' in new_config.keys():
        new_config_file.append(f"default_dir: {new_config['default_dir']}")
    if 'color_module' in new_config.keys():
        new_config_file.append(f"color_module: {new_config['color_module']}")
    if 'other_dir' in new_config.keys():
        new_config_file.append(f"other_dir:")
        for item in new_config['other_dir']:
            new_config_file.append(f"{indent}- {item}")
    if 'default_files' in new_config.keys() or 'ignore_files' in new_config.keys():
        new_config_file.append(f"notes:")
    if 'default_files' in new_config.keys():
        new_config_file.append(f"{indent}default_files:")
        for item in new_config['default_files']:
            new_config_file.append(f"{indent*2}- {item}")
    if 'ignore_files' in new_config.keys():
        new_config_file.append(f"{indent}ignore_files:")
        for item in new_config['ignore_files']:
            new_config_file.append(f"{indent*2}- {item}")
    if 'html_cmds' in new_config.keys():
        new_config_file.append(f"html_cmds:")
        for cmd, strings in new_config['html_cmds'].items():
            new_config_file.append(f"{indent}{cmd}:")
            for string in strings:
                new_config_file.append(f"{indent*2}- {string}")
    if 'colors' in new_config.keys():
        new_config_file.append(f"colors:")
        for cmd, strings in new_config['colors'].items():
            new_config_file.append(f"{indent}{cmd}:")
            for string in strings:
                new_config_file.append(f"{indent*2}- {string}")

    # new_config_file

    # print(json.dumps(new_config,indent=2))
    with open(master_rc['rc_file'], 'w') as nycf:
        nycf.writelines("%s\n" % place for place in new_config_file)

    # with open(master_rc['rc_file'], 'w') as nycf:
    #         yaml.dump(new_config, nycf, default_flow_style=False)
    exit()





## Auto disable color
def auto_disable():
    '''
    The fstat and statvfs commands return input, stdout, stderror.
    If the output is not to terminal the escape characters are removed.
    '''
    if os.fstat(0) != os.fstat(1) or os.fstat(0) != os.fstat(2):
        args.color = False
auto_disable()



## SEARCH BOOLEAN
def and_search(line, search_lst):
    # Search for elements as an AND &&.

    # Case sensitivity:
    if args.sensitive:
        if all([re.search(s,line) for s in search_lst]):
            return True

    else:
        if all([re.search(s.upper(),line.upper()) for s in search_lst]):
            return True

    return False


def or_search(line, search_lst):
    # Search for elements as an OR ||.

    # Case sensitivity:
    if args.sensitive:
        if any([re.search(s,line) for s in search_lst]):
            return True

    else:
        if any([re.search(s.upper(),line.upper()) for s in search_lst]):
            return True

    return False


def not_search(line, search_lst):
    # Remove search elements.

    # Case sensitivity:
    if args.sensitive:
        if any([re.search(s,line) for s in search_lst]):
            return True

    else:
        if any([re.search(s.upper(),line.upper()) for s in search_lst]):
            return True

    return False


def ooo_search(line, search_el):
    # Regex Order Of Operations search for elements.

    # Case sensitivity:
    if args.sensitive:
        if re.search(search_el, line):
            return True

    else:
        if re.search(search_el.upper(), line.upper()):
            return True

    return False



## PULLING FILES
def pull_files(directory):
    # Return all files from the specefied directory/s.

    file_lst = []
    dir_lst = []

    for path in directory:
        guide_files = os.listdir(path)

        # Normal path
        for fl in guide_files:

            # Skip if the file is in the ignore list
            if fl in rc_file['ignore_files']:
                continue

            # If it is a hidden file skip it.
            if fl.startswith('.'):
                continue

            file_name = path + fl

            if os.path.isdir(file_name):
                # If the file is actually a directory, save it as a directory instaed
                dir_lst.append((path,fl))

            if os.path.isfile(file_name):
                # If the file is truly a file, save it
                file_lst.append((path,fl))

        # Recursive path
        if args.recursive:
          # If the recursive arg is True itterate through the directories until every file has been added

            while len(dir_lst) > 0:
              directory_pop = dir_lst.pop()

              for file_orig_pop in os.listdir('/'.join(directory_pop)):
                  file_pop = directory_pop[0] + '/' + directory_pop[1] + '/' + file_orig_pop

                  if os.path.isdir(file_pop):
                      # In the directory if the file is actaully a directory, add it to the list
                      dir_lst.append((directory_pop[0] + directory_pop[1], file_orig_pop))

                  if os.path.isfile(file_pop):
                      # In the directory if the file is a file, add it to the file list
                      file_lst.append((directory_pop[0] + directory_pop[1], file_orig_pop))

    # Skip if its not a markdown file and the nonmarkdown file is false
    if not args.nonmarkdown:
        file_lst = [(path, fl) for path, fl in file_lst if \
            any([True for suf in rc_file['default_files'] if fl.endswith(suf)])]

    return file_lst



## PRINTING
def printit(greplen = 10):
    '''
    Print the desired search to the terminal.
    There is a text seporator (###...) for the search results.
    The files are collected in print_list and then printed at the end.
    '''
    print_list = []

    if args.grep == 1 or args.grep == None:
        # Basic grep replicator.

        for ro in readout:
            print_list.append(f"{ro['file']} :\t{ro['lines'][:-1]}")

    elif args.grep == 2:
        # Grep -C10 (-A10 -B10) replicator.

        for ro in readout:
            print_list.append('\n' + config['string_break'])
            print_list.append(f'{ro}')

            with open(ro['file'], 'r') as f:
                contents = f.readlines()
            paragraph = contents[ro['index'] - greplen:ro['index'] + greplen]

            for pg in paragraph:
                print_list.append(pg[:-1])

    elif args.grep == 3:
        # Prints the list of files and then each files contents to the terminal.

        file_list = []
        md = True

        print_list.append(f"List of files")

        for ro in readout:
            if ro['file'] not in file_list:
                print_list.append(f"{ro['file'][:-1]}")
                file_list.append(ro['file'])

        print_list.append(f"Printout of files")
        for fl in file_list:
            print_list.append('\n' + config['string_break'])
            print_list.append(f'{ro}')

            with open(fl, 'r') as f:
                contents = f.readlines()

            contents = markdown(contents)

            for el in contents:
                print_list.append(f"{el[:-1]}")

    elif args.grep >= 4:

        file_list = []
        print_list.append(f"List of files")

        for ro in readout:
            if ro['file'] not in file_list:
                print_list.append(f"{ro['file']}")
                file_list.append(ro['file'])


    # Finally printing
    grep_keys = []

    # Setting up color setting
    if args.search != []:
        grep_keys.extend(args.search)
    if args.AND != None:
        grep_keys.extend(args.AND)
    if args.OR != None:
        grep_keys.extend(args.OR)

    for el in print_list:
        # Formatting each line

        if args.NOT != None:
            if not_search(el,args.NOT):
                continue

        if args.color:
            # If colors turned on

            if args.grep == 1 or args.grep == None:
                # Formatting files for grep ==1 & None require different searches
                splitout = el.split(':')
                splitout[0] = FILE + splitout[0] + SC.clc
                el = ':'.join(splitout)

            else:
                # Formatting files for other grep types
                if all([string in el for string in ['file', 'index', 'lines']]):
                  el = FILE  + el  + SC.clc

            for gk in grep_keys:
                # Formatting greps if they are found
                colord_string = GREP + gk + SC.clc
                el = colord_string.join(el.split(gk))

                # Formatting page breaks
                if config['string_break'] in el:
                    el = HEADER + config['file_break'] + SC.clc

        else:
            # If there is a page break but color is False
            if config['string_break'] in el:
                el = '\n' + config['file_break']

        # Finally printing!
        print(el)



# Markdown tables were complicated so I built something to deal with them better.
def markdown_table(cont):
    '''
    Because markdown tables are complicated I have the script run any table it finds through this.
    It sets the column width the same.
    It is possible it will break if there are multiple rows but I havnt tested it yet and I am just now thinking about it.
    '''
    table_len = []
    table = []
    table_out = []
    master_table_len = []
    for line in cont:
        table_len.append([len(e) for e in line.split('|')])
        table.append([e for e in line.split('|')])
    master_table_len = [0 for el in table_len[0]]
    for dex, line in enumerate(table):
        if len(line) < len(master_table_len):
            table[dex].append('')

    for dex, ln in enumerate(table_len):
        for dex2, el in enumerate(ln):
            master_table_len[dex2] = max(el, master_table_len[dex2])

    for dex1, line in enumerate(table):
        for dex2, el in enumerate(line):
            while len(table[dex1][dex2]) < master_table_len[dex2] + 1:
                if dex1 == 1:
                    if ' ' in table[dex1][dex2]:
                        table[dex1][dex2] = ''.join(['-' for c in table[dex1][dex2]])
                    table[dex1][dex2] = table[dex1][dex2] + '-'
                else:
                    table[dex1][dex2] = table[dex1][dex2] + ' '
    for line in table:
        table_out.append('|'.join(line))
    return table_out


def markdown_cmd(cmds):
    new_text = []
    valid_html_cmds = master_rc['html_cmds']

    for cmd in cmds.split(','):
        while cmd.startswith(' '):
            cmd = cmd[1:]
        while cmd.endswith(' '):
            cmd = cmd[:-1]
        if any([True for valid in valid_html_cmds.keys() if cmd.upper() == valid.upper()]):
            for i,j in valid_html_cmds.items():
                if cmd.upper() == i.upper():
                    for color_update in master_rc['html_cmds'][i]:
                        try:
                            new_text.append(
                                SC.__dict__[color_update]
                            )
                        except KeyError:
                            pass
        else:
            new_text.append('')
    return ''.join(new_text)


def markdown(cont):
    '''
    This is run every time markdown files are being parsed.
    So far I have parsed tables, backtick strings and block text (` and ```), Notes (>), page breaks, and ignoring hidden comments.
    There are more markdown elements out there but they did not benefit much by being separated out.
    I will happily update this section if people want additions!
    '''
    if not args.color:
      # If colors are turned off, just print everything in the file unchanged

        for line in cont:
            print(line[:-1])

        return ''

    # Setting up markdown specific flags and regex strings
    # Flags
    is_block = config['markdown_flags']['is_block']
    table_header = config['markdown_flags']['table_header']
    table_toggle = config['markdown_flags']['table_toggle']
    table_flag = config['markdown_flags']['table_flag']
    hidden_flag = config['markdown_flags']['hidden_flag']
    html_cmd = config['markdown_flags']['html_cmd']


    # Regex
    header_s = config['regex_strings']['header_s']
    break_s = config['regex_strings']['break_s']
    note_s = config['regex_strings']['note_s']
    line_s = config['regex_strings']['line_s']
    hidden_start_s = config['regex_strings']['hidden_start_s']
    hidden_end_s = config['regex_strings']['hidden_end_s']
    html_cmd_start_s = config['regex_strings']['html_cmd_start_s']
    html_cmd_end_s = config['regex_strings']['html_cmd_end_s']
    # header_s        "'^ *?##* .*"
    # break_s         "'^ *(----*|\*\*\*\**|____*) *$"
    # note_s          "'^ *>>*"
    # hidden_s        "'^ {0,3}\[//\]: # \(.*"
    # line_s          "'.*\!?[.*\]\(.*\)"
    # html_cmd_start  "<!--"
    # html_cmd_end    "-->"

    # Markdown list
    md_out = []

    for dex, line in enumerate(cont):
        line = line[:-1]

        if dex == 0:
            # Seporate from the previous file if there are multiple
            md_out.append('\n' + HEADER + config['file_break'] + SC.clc + '\n')

        if re.search(hidden_start_s, line) or hidden_flag:
            # Ignore hidden text

            if re.search(hidden_start_s, line):
                hidden_flag = True

            if re.search(hidden_end_s, line):
                hidden_flag = False
            continue

        if re.search(html_cmd_start_s, line) or html_cmd:
            cmd_list = []
            new_line = []
            temp_list1 = re.split(html_cmd_start_s,line)
            for element in temp_list1:
                if element == '':
                    html_cmd = True
                elif re.search(html_cmd_end_s, element):
                    temp_list2 = re.split(html_cmd_end_s, element)
                    if len(temp_list2) != 2:
                        # print(temp_list2)
                        raise ValueError('The lenght of this element is not exactly 2 which is unexpected and should be investigated')
                    new_line.append(markdown_cmd(temp_list2[0]))
                    new_line.append(temp_list2[1])
                    html_cmd = False
                else:
                    new_line.append(element)
            if html_cmd:
                continue
            line = ''.join(new_line)


        if re.search(header_s, line):
            # Section headers
            # Right now I dont have a good way to increase the text size so i just make the section headers stand out.
            # Markdown only recognises headers up to the 6th level.
            line = line.strip()
            head_intensity = len(re.findall('^##*', line)[0])
            line = line.strip('#')

            if head_intensity == 1:
                line = line + '\n' + config['page_break']

            elif head_intensity == 2:
                line = '   ' + line + '\n' + '                                        '

            elif head_intensity == 3:
                line = '      ' + line

            elif head_intensity == 4:
                line = '         ' + line

            elif head_intensity == 5:
                line = '            ' + line

            elif head_intensity == 6:
                line = '               ' + line

            line =  '   ' + HEADER + SC.underline + line[1:] + SC.clc

        if re.search(break_s, line):
            # Page break
            line = HEADER + SC.underline + config['page_break'] + SC.clc

        if re.search(note_s, line):
            # Note
            line = line.strip().strip('>')
            line = NOTE + '| ' + line + SC.clc

        if len(re.findall('\|', line)) > 2:
            # Tables
            '''
            When a table is found, all the rest of the table is pulled and run through the markdown table thing above.
            This is achieved by the first line of a table setting the table flag True.
            The script itterates through the lines of the rest of the file to pull the reat of the table.
            The entier table is run through the markdown table function above.
            The table is returned and formatted here.
            When the script keeps itterating through elements of the table it ignores them because the table flag is still True.
            When the end of the table is reached the table flag is set to False until the next table is found.
            This could cause the script to error if the end of the file is part of the table but should be fine if there is even one line of whitespace.
            '''
            if table_flag:
                continue

            table_flag = True
            table = []
            table_out = []
            i = dex

            while True:
                table.append(cont[i][:-1])
                if i == len(cont) - 1:
                    break
                # print(i, dex, len(cont))
                if len(re.findall('\|', cont[i+1])) <= 2:
                    break
                i += 1

            table = markdown_table(table)

            for el in table:

                if table_header:
                    el = SC.bold + SC.underline + TABLE1 + el + SC.clc
                    table_header = False
                    table_toggle = False

                if re.search('^(\||-| )*$', el):
                    continue

                else:

                  if table_toggle:
                      el = SC.clc + TABLE2 + el + SC.clc
                      table_toggle = False

                  else:
                      el = SC.clc + TABLE1 + el + SC.clc
                      table_toggle = True

                table_out.append(el)

            line = '\n'.join(table_out)

            if len(re.findall('\|', cont[dex+1])) == 0:
                table_header = True
                table_toggle = False
                line = line + SC.clc

        if len(re.findall('`', line)) > 0:
            # Has backticks
            line = re.split('`|```', line)
            while len(line) > 1:
                if is_block:
                    line = [SC.clc.join(line[:2])] + line[2:]
                    is_block = False
                else:
                    line = [BLOCK.join(line[:2])] + line[2:]
                    is_block = True
            line = line[0]

        md_out.append(line)
    cont, md_out = md_out, []
    for el in cont:
        print(el)
    return md_out



## RUNNING FILE FUNCTION
readout = []
guide_files = pull_files(directory)



## INTERPRETING ARGS
# If no search pervided
if args.search == [] and \
    args.AND == None and \
    args.OR == None and \
    args.list == None and \
    args.config == None:

    for fl in guide_files:
        print(f"{fl[0]}/{fl[1]}")

    # Returns help if no args provided.
    print(f'\n\t' + SC.yellow + 'No args provided. All files are printed above. The help is printed below' + SC.clc + '\n')
    parser.print_help()


# If there are list or order specific search elements
elif args.list != None:

    # Every time an argument is used the file search pool gets reduced.
    guide_files_list = guide_files
    guide_list = []
    initial_readout = []

    for el in args.list:

        for gf in guide_files_list:

            with open(gf[0] + '/' + gf[1], 'r') as f:
                contents = f.readlines()

                for index, line in enumerate(contents):

                    if ooo_search(line,el):
                        initial_readout.append({'file':gf[0] + '/' + gf[1], 'index':index, 'lines':line})
                        guide_list.append(gf[0] + '/' + gf[1])

        if el != args.list[-1]:
            # While still searching through the args.list the folowing occures.
            guide_files_list = []
            initial_readout = []
            # File lists get reduced and filter results as well.

            for fl in set(guide_list):
                rebuild = fl.split('/')
                rebuild = ['/'.join(rebuild[:-1]),rebuild[-1]]
                guide_files_list.append(rebuild)
            guide_list = []

    readout = initial_readout


# If AND, OR, or NOT are provided
else:

    # If there is an AND search
    if args.AND:

        for gf in guide_files:

            with open(gf[0] + '/' + gf[1], 'r') as f:
                contents = f.readlines()

                for index, line in enumerate(contents):

                    if and_search(line,args.AND):
                        readout.append({'file':gf[0] + '/' + gf[1], 'index':index, 'lines':line})

    # If there is an OR search
    if args.OR:

        for gf in guide_files:

            with open(gf[0] + '/' + gf[1], 'r') as f:
                contents = f.readlines()

                for index, line in enumerate(contents):

                    if or_search(line,args.OR):
                        readout.append({'file':gf[0] + '/' + gf[1], 'index':index, 'lines':line})

    # If there is a search but no AND or OR
    if args.search != []:

        for gf in guide_files:

            with open(gf[0] + '/' + gf[1], 'r') as f:
                contents = f.readlines()

                for index, line in enumerate(contents):

                    # By default run an OR search
                    if or_search(line,args.search):
                        readout.append({'file':gf[0] + '/' + gf[1], 'index':index, 'lines':line})

        for is_fl in args.search:
            if os.path.isfile(is_fl):
                with open(is_fl, 'r') as f:
                    contents = f.readlines()
                markdown(contents)
                #print('ISFILE\n\n\n\n\n\n')

# At the end of everything the print function is called

printit()
# print(args)
