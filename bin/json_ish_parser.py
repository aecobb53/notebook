
import json
import datetime
import uuid
import argparse
import re

# Argparse
aparse = argparse.ArgumentParser(description='Task Warrior TMUX wrapper')
aparse.add_argument('args', nargs='*')
args = aparse.parse_args()

def json_ish_parse(string):
    output1 = [[]]
    output2 = []
    indent_length = 4
    tab = ' ' * indent_length
    index = 0
    set_indent = 0
    current_indent = 0
    in_quotes = []

    # for character in args.args[0]:
    for character in string:
        if character in [')', ']', '}']:
            index += 1
            set_indent -= 1
            current_indent = set_indent
            output1.append([])
        if len(output1[index]) == 0:
            output1[index].append(current_indent * tab)
        if character == ' ' and not in_quotes:
            continue
        output1[index].append(character)
        if character == ',':
            index += 1
            output1.append([])
        if character in ['(', '[', '{']:
            index += 1
            set_indent += 1
            current_indent = set_indent
            output1.append([])
        if character in ['"', "'"]:
            if not in_quotes:
                in_quotes.append(character)
            else:
                if character == in_quotes[-1]:
                    in_quotes.pop(-1)
                else:
                    in_quotes.append(character)

    for l in output1:
        if l != []:
            output2.append(''.join(l))
    return output2

output2 = json_ish_parse(' '.join(args.args))

for l in output2:
    print(l)
