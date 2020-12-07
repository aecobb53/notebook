# dict_one = {
#     "default_files": [
#         ".md"
#     ],
#     "ignore_files": [
#         "README.md"
#     ],
#     "FILE": [
#         "magenta"
#     ],
#     "HEADER": [
#         "blue"
#     ],
#     "GREP": [
#         "bright_red"
#     ],
#     "BLOCK": [
#         "\\u001b[48;5;243;1m",
#         "\\u001b[38;5;232m"
#     ],
#     "TABLE1": [
#         "\\u001b[48;5;251;1m",
#         "\\u001b[38;5;236m"
#     ],
#     "TABLE2": [
#         "\\u001b[48;5;248;1m",
#         "\\u001b[38;5;239m"
#     ],
#     "NOTE": [
#         "\\u001b[38;5;246m"
#     ]
# }

# dict_two = {
#     "default_files": [
#         ".md"
#     ],
#     "FILE": [
#         "magenta"
#     ],
#     "HEADER": [
#         "blue"
#     ],
#     "GREP": [
#         "bright_red"
#     ],
#     "BLOCK": [
#         "\\u001b[48;5;243;1m",
#         "\\u001b[38;5;232m"
#     ],
#     "TABLE1": [
#         "\\u001b[48;5;251;1m",
#         "\\u001b[38;5;236m"
#     ],
#     "TABLE2": [
#         "\\u001b[48;5;248;1m",
#         "\\u001b[38;5;239m"
#     ],
#     "NOTE": [
#         "\\u001b[38;5;246m"
#     ],
#     "default_dir": "/home",
#     "color_module": 256,
#     "other_dir": [
#         "/home/acobb/git",
#         "/home"
#     ],
#     "notes": {
#         "default_files": [
#             ".md",
#             ".txt"
#         ],
#         "ignore_files": [
#             ".txt"
#         ]
#     },
#     "html_cmds": {
#         "blue": [
#             "blue"
#         ]
#     },
#     "colors": {
#         "FILE": [
#             "red",
#             "back_white",
#             "italic"
#         ],
#         "white": [
#             "grey",
#             "italic"
#         ]
#     }
# }


# dict_one = {
#     'FIRSTLAYERDICT': {
#         'SECONDLAYERDICT': {
#             'THIRDLAYERDICT':'FOURTHLAYERSTRING'
#         }
#     },
#     '2FIRSTLAYERDICT': {
#         '2SECONDLAYERDICT': {
#             '2THIRDLAYERDICT':'2FOURTHLAYERSTRING'
#         }
#     },
#     '2onedct': {
#         '2twodict': {
#             '2threedict':'2fourdict'
#         }
#     },
#     'FIRSTLAYERLIST': [
#         'SECONDLAYERSTRING',
#         'THIRDLAYERSTRING',
#         'FOURTHLAYERSTRING',
#     ],
#     '2FIRSTLAYERLIST': [
#         '2SECONDLAYERSTRING',
#         '2THIRDLAYERSTRING',
#         '2FOURTHLAYERSTRING',
#     ]
# }
# dict_two = {
#     'FIRSTLAYERDICT': {
#         'SECONDLAYERDICT': {
#             'THIRDLAYERDICT':'FOURTHLAYERSTRING'
#         }
#     },
#     '2FIRSTLAYERDICT': {
#         '2SECONDLAYERDICT': {
#             '2THIRDLAYERDICT':'2FOURTHLAYERSTRING'
#         }
#     },
#     'FIRSTLAYERLIST': [
#         'SECONDLAYERSTRING',
#         'THIRDLAYERSTRING',
#         'FOURTHLAYERSTRING',
#     ],
#     '2FIRSTLAYERLIST': [
#         '2SECONDLAYERSTRING',
#         '2THIRDLAYERSTRING',
#         '2FOURTHLAYERSTRING',
#     ],
#     '2oneline': [
#         '2twolist',
#         '2twolist',
#         '2twolist',
#     ]
# }

dict_one = {
    'FIRSTLAYERDICT': "1string"
}
dict_two = {
    'FIRSTLAYERDICT': "2string"
}


def update_config(object1, object2):
    if isinstance(obj)
    # # newobject = type(object1)
    # print(type(object1), type(object2))
    # if isinstance(object1, dict):
    #     for key in object1.keys():
    #         print(f'first_key {key}')
    #         if key in object2.keys():
    #             print(f'keys match')
    #             if update_config(object1[key], object2[key]):
    #                 newobject = {key:object2[key]}
    #             # print(object1[key], object2[key])
    # # if isinstance(object1, list)
    # elif isinstance(object1, str) or isinstance(object1, int):
    #     print('done recursing')
    #     # newobject
    #     return True
    # else:
    #     return newobject

print(update_config(dict_one, dict_two))