


def set_str_length(string, length):
    while len(string) < length:
        string = string + ' '
    return string


class StringColors:
    """
    This class is to help spice up python terminal text output. 
    I reccomend importing the class and saving it to something shorter like 'SM'
    This allows you to use print(SM.RED + 'String here' + SM.clc).
    It is easier. 
    There are four sections below: 8 bit / 16 bit / 256 bit / Decorators. 
    Bits refer to the types of clors and Decorators are styles (bold, underline, ...)
    The terminal windows we have support upu to 256 bit colors. 
    I am lead to believe this is not the case with all systems. 
    If you discover the 256 bit coors are not working you may need to reduce to the 16 or 8 bit. 
    If you look closely you will notice the 16 bit colors are the same as the 8 bit colors but half are brighter. 
    The brighter function just alters the forground color to make it look slightly brighter. 

    Each bit type 8, 16, 256 starts with a string starter. 
    8 & 16 are the same and work with the 256's starter, but it does not go the other way.
    The way to make any color brighter is to change the 'm' tag to a ';1m' tag.
    """


    def __init__(self):
        self.clc = '\u001b[0m'
        self.color_table_starter = '\u001b['
        self.curer = 'm'
        self.light_curer = ';1m'
        self.color = None
        self.light_color = None
        self.background = None
        self.light_background = None
        self.bits = None

    
    def set_styles(self):
        # Formats
        self.set_color('normal',        0, 'style')
        self.set_color('bold',          1, 'style')
        self.set_color('faint',         2, 'style')
        self.set_color('italic',        3, 'style')
        self.set_color('underline',     4, 'style')
        self.set_color('blinking',      5, 'style')
        self.set_color('Unknown',       6, 'style')
        self.set_color('hilight',       7, 'style')
        self.set_color('hide',          8, 'style')
        self.set_color('strikethrough', 9, 'style')


    def set_color(self, attribute, code, *args):
        """
        color
        background
        light
        style
        """
        # print(f"attribute:{attribute}, code:{code}, bits:{self.bits}, args:{args}")
        color = False
        background = False
        light = False
        style = False

        if args == ():
            color = True

        leading = None
        trailing = None

        for arg in args:
            # print(f"arg::{arg}")
            if arg.lower() in ['color']:
                color = True
            if arg.lower() in ['bright', 'light']:
                light = True
            if arg.lower() in ['background']:
                background = True
            if arg.lower() in ['style', 'format']:
                style = True

        if not color and not background and not light and style and \
            self.bits in ['256bit', '16bit', '8bit']:
            # print('style')
            leading = self.color_table_starter
            trailing = self.curer
        elif color and not background and not light and not style and \
            self.bits in ['256bit', '16bit', '8bit']:
            # print('color')
            leading = self.color
            trailing = self.curer
        elif color and not background and light and not style and \
            self.bits in ['256bit', '16bit', '8bit']:
            # print('light color')
            leading = self.light_color
            trailing = self.light_curer
        elif not color and background and not light and not style and \
            self.bits in ['256bit', '16bit', '8bit']:
            # print('background')
            leading = self.background
            trailing = self.curer
        elif not color and background and light and not style and \
            self.bits in ['256bit', '16bit', '8bit']:
            # print('light brackground')
            leading = self.light_background
            trailing = self.light_curer
        else:
            raise ValueError('You are rquesting a format that is not used')
        
        code = leading + str(code) + trailing
        super().__setattr__(attribute, code)


    def print_pallet(self):
        max_length = 0
        color_list = []
        for string, code in self.__dict__.items():
            if string in [
                'color_table_starter',
                'curer',
                'light_curer',
                'color',
                'light_color',
                'background',
                'light_background',
                'bits',
                ]:
                continue
            # print(len(string),string)
            max_length = max(max_length, len(string))
            color_list.append(string)

        for string, code in self.__dict__.items():
            if string in color_list:
                print(f"{code}{set_str_length(string, max_length)}\t|{self.clc}{string}")

    
class Bit8(StringColors):
    """
    8 bit specific string modifiers
    """

    def __init__(self):
        super().__init__()
        self.color = '\033['
        self.light_color = '\033['
        self.background = '\033['
        self.light_background = '\033['
        self.bits = '8bit'

        self.set_styles()

        # Colors
        self.set_color('black',     30, 'color')
        self.set_color('red',       31, 'color')
        self.set_color('green',     32, 'color')
        self.set_color('yellow',    33, 'color')
        self.set_color('blue',      34, 'color')
        self.set_color('magenta',   35, 'color')
        self.set_color('cyan',      36, 'color')
        self.set_color('white',     37, 'color')

        # Background colors
        self.set_color('back_black',     40, 'background')
        self.set_color('back_red',       41, 'background')
        self.set_color('back_green',     42, 'background')
        self.set_color('back_yellow',    43, 'background')
        self.set_color('back_blue',      44, 'background')
        self.set_color('back_magenta',   45, 'background')
        self.set_color('back_cyan',      46, 'background')
        self.set_color('back_white',     47, 'background')


    def color_table(self):
        for code in range(88):
            print(
                self.color_table_starter + 
                str(code) + 
                self.curer + 
                str(code) + 
                self.clc
                )


class Bit16(StringColors):
    """
    16 bit specific string modifiers
    """

    def __init__(self):
        super().__init__()
        self.color = '\033['
        self.light_color = '\033['
        self.background = '\033['
        self.light_background = '\033['
        self.bits = '16bit'

        self.set_styles()

        # Colors
        self.set_color('black',     30, 'color')
        self.set_color('red',       31, 'color')
        self.set_color('green',     32, 'color')
        self.set_color('yellow',    33, 'color')
        self.set_color('blue',      34, 'color')
        self.set_color('magenta',   35, 'color')
        self.set_color('cyan',      36, 'color')
        self.set_color('white',     37, 'color')

        # Background colors
        self.set_color('back_black',     40, 'background')
        self.set_color('back_red',       41, 'background')
        self.set_color('back_green',     42, 'background')
        self.set_color('back_yellow',    43, 'background')
        self.set_color('back_blue',      44, 'background')
        self.set_color('back_magenta',   45, 'background')
        self.set_color('back_cyan',      46, 'background')
        self.set_color('back_white',     47, 'background')

        # Bright colors
        self.set_color('bright_black',     90, 'color', 'bright')
        self.set_color('bright_red',       91, 'color', 'bright')
        self.set_color('bright_green',     92, 'color', 'bright')
        self.set_color('bright_yellow',    93, 'color', 'bright')
        self.set_color('bright_blue',      94, 'color', 'bright')
        self.set_color('bright_magenta',   95, 'color', 'bright')
        self.set_color('bright_cyan',      96, 'color', 'bright')
        self.set_color('bright_white',     97, 'color', 'bright')

        # Bright background colors
        self.set_color('bright_back_black',     100, 'background', 'bright')
        self.set_color('bright_back_red',       101, 'background', 'bright')
        self.set_color('bright_back_green',     102, 'background', 'bright')
        self.set_color('bright_back_yellow',    103, 'background', 'bright')
        self.set_color('bright_back_blue',      104, 'background', 'bright')
        self.set_color('bright_back_magenta',   105, 'background', 'bright')
        self.set_color('bright_back_cyan',      106, 'background', 'bright')
        self.set_color('bright_back_white',     107, 'background', 'bright')


    def color_table(self):
        str_len = 3
        for code in range(128):
            print(
                '| ' + 
                self.color_table_starter + 
                str(code) + 
                self.curer + 
                set_str_length(str(code), str_len) + 
                ' | ' + 
                self.clc + 

                self.color_table_starter + 
                str(code) + 
                self.light_curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 
                ' |'
                )


class Bit256(StringColors):
    """
    256 bit specific string modifiers
    """

    def __init__(self):
        super().__init__()
        self.color = '\u001b[38;5;'
        self.light_color = '\u001b[38;5;'
        self.background = '\u001b[48;5;'
        self.light_background = '\u001b[48;5;'
        self.bits = '256bit'

        self.set_styles()

        # Colors
        self.set_color('black',     0, 'color')
        self.set_color('red',       1, 'color')
        self.set_color('green',     2, 'color')
        self.set_color('yellow',    3, 'color')
        self.set_color('blue',      4, 'color')
        self.set_color('magenta',   5, 'color')
        self.set_color('cyan',      6, 'color')
        self.set_color('white',     7, 'color')

        # Background colors
        self.set_color('back_black',     8, 'background')
        self.set_color('back_red',       9, 'background')
        self.set_color('back_green',     10, 'background')
        self.set_color('back_yellow',    11, 'background')
        self.set_color('back_blue',      12, 'background')
        self.set_color('back_magenta',   13, 'background')
        self.set_color('back_cyan',      14, 'background')
        self.set_color('back_white',     15, 'background')

        # Bright colors
        self.set_color('bright_black',     0, 'color', 'bright')
        self.set_color('bright_red',       1, 'color', 'bright')
        self.set_color('bright_green',     2, 'color', 'bright')
        self.set_color('bright_yellow',    3, 'color', 'bright')
        self.set_color('bright_blue',      4, 'color', 'bright')
        self.set_color('bright_magenta',   5, 'color', 'bright')
        self.set_color('bright_cyan',      6, 'color', 'bright')
        self.set_color('bright_white',     7, 'color', 'bright')

        # Bright background colors
        self.set_color('bright_back_black',     8, 'background', 'bright')
        self.set_color('bright_back_red',       9, 'background', 'bright')
        self.set_color('bright_back_green',     10, 'background', 'bright')
        self.set_color('bright_back_yellow',    11, 'background', 'bright')
        self.set_color('bright_back_blue',      12, 'background', 'bright')
        self.set_color('bright_back_magenta',   13, 'background', 'bright')
        self.set_color('bright_back_cyan',      14, 'background', 'bright')
        self.set_color('bright_back_white',     15, 'background', 'bright')


    def color_table(self):
        """
        Print out a table of all available colors. 
        """

        str_len = 3
        print("| color | bright | background | bright background |")
        for code in range(257):
            print(
                '| ' + 
                self.color + 
                str(code) + 
                self.curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                self.light_color + 
                str(code) + 
                self.light_curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' |' + 

                self.background + 
                str(code) + 
                self.curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                self.light_background + 
                str(code) + 
                self.light_curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' |'
                )

    def print_color_comparison(self, number_list, set_color, set_background):
        """
        Compare similar colors to the selected color as well as backgrounds. 
        """

        str_len = 3
        print('\n\n\n')
        print("| regular ||| bright |")
        print("| selection | selected | backgrounds | background | -- code")
        for code in number_list:
            print(
                '| ' + 
                self.color + 
                str(code) + 
                self.curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                set_color + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                self.background + 
                str(code) + 
                self.light_curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                set_background + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                '  |||  ' +

                self.light_color + 
                str(code) + 
                self.curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                set_color + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                self.light_background + 
                str(code) + 
                self.light_curer + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | ' + 

                set_background + 
                set_str_length(str(code), str_len) + 
                self.clc + 

                ' | -- ' + 

                str(code)
            )

    def color_selector(self, *args):
        """
        Similar colors to help selection. 
        If the provided list of strings is found in the color pallets below they are compared. 

        """

        print(args)

        if len(args) == 0:
            args = (
                'black',
                'red',
                'green',
                'yellow',
                'blue',
                'megenta',
                'cyan',
                'white',
            )

        for args in args:

            if args in ['black']:
                # K
                self.print_color_comparison(
                    [0] + 
                    [8] + 
                    list(range(231,256)), 
                    self.black, 
                    self.back_black
                    )

            if args in ['red']:
                # R
                self.print_color_comparison(
                    [1] + 
                    [9] + 
                    list(range(52, 64)) + 
                    list(range(88, 100)) + 
                    list(range(124, 142)) + 
                    list(range(160, 178)) + 
                    list(range(196, 220)), 
                    self.red, 
                    self.back_red
                    )

            if args in ['green']:
                # G
                self.print_color_comparison(
                    [2] + 
                    [10] + 
                    list(range(22, 52)) + 
                    list(range(64, 88)) + 
                    list(range(112, 124)) + 
                    list(range(154, 160)) + 
                    list(range(190, 196)),
                    self.green, 
                    self.back_green
                    )

            if args in ['yellow']:
                # Y
                self.print_color_comparison(
                    [3] + 
                    [11] + 
                    list(range(58, 64)) + 
                    list(range(100, 112)) + 
                    list(range(130, 160)) + 
                    list(range(166, 196)) + 
                    list(range(202, 232)),
                    self.yellow, 
                    self.back_yellow
                    )

            if args in ['blue']:
                # B
                self.print_color_comparison(
                    [4] + 
                    [12] + 
                    list(range(17, 52)) + 
                    list(range(52, 124)),
                    self.blue, 
                    self.bacl_blue
                    )

            if args in ['magenta']:
                # M
                self.print_color_comparison(
                    [5] + 
                    [13] + 
                    list(range(52, 64)) + 
                    list(range(88, 113)) + 
                    list(range(124, 148)) + 
                    list(range(160, 190)) + 
                    list(range(196, 226)),
                    self.magenta, 
                    self.back_magenta
                    )

            if args in ['cyan']:
                # C
                self.print_color_comparison(
                    [6] + 
                    [14] + 
                    list(range(17, 52)) + 
                    list(range(64, 88)) + 
                    list(range(106, 124)),
                    self.cyan, 
                    self.back_cyan
                    )

            if args in ['white']:
                # W
                self.print_color_comparison(
                    [7] + 
                    [15] + 
                    list(range(231,256)), 
                    self.white, 
                    self.back_white
                    )
