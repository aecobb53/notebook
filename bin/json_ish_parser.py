
import json
import datetime
import uuid
import argparse
import re

# from sys import argv

# # print(argv)
# # print(argv[0])
# # print(argv[1])
# # print(argv[2])


# Argparse
aparse = argparse.ArgumentParser(description='Task Warrior TMUX wrapper')
aparse.add_argument('args', nargs='*')
args = aparse.parse_args()

# print(args)
print('')

output1 = [[]]
output2 = []
indent_length = 4
tab = ' ' * indent_length
# tab = '----'
index = 0
set_indent = 0
current_indent = 0

for c in args.args[0]:
    if c in [')', ']', '}']:
        index += 1
        set_indent -= 1
        current_indent = set_indent
        output1.append([])
    if len(output1[index]) == 0:
        output1[index].append(current_indent * tab)
    output1[index].append(c)
    if c == ',':
        index += 1
        output1.append([])
    if c in ['(', '[', '{']:
        index += 1
        set_indent += 1
        current_indent = set_indent
        output1.append([])

for l in output1:
    if l != []:
        output2.append(''.join(l))

for l in output2:
    print(l)
