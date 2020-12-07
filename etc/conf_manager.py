import yaml
import json


def update_config(config1, config2):
    newconfig = config1
    keyvalue = [
        'default_dir',
        'color_module',
        'rc_file',
    ]
    listupdate = [
        'other_dir',
    ]
    deep_listupdate = [
        'notes',
        'html_cmds',
        'colors',
    ]
    dictupdate = {}
    for key, value in config2.items():
        # print(key,value)
        if key not in newconfig.keys():
            # print('    not in newconfig')
            newconfig[key] = value
            continue
        if key in keyvalue:
            # print('    key in keyvalue')
            newconfig[key] = config2[key]
            continue
        if key in listupdate:
            # print('    key in list update')
            if key not in newconfig.keys():
                newconfig.update({key:[]})
            newconfig[key].append(value)
            continue
        if key in deep_listupdate:
            # print('    key in deep list update')
            # print(type(value))
            for cmd, lst in value.items():
                # print('        ', cmd, lst)
                if cmd not in newconfig[key].keys():
                    newconfig[key].update({cmd:[]})
                for item in lst:
                    newconfig[key][cmd].append(item)
            continue
        # print('not found')
    return newconfig

# # dct1 = {
# #     'main':'first',
# #     'confirm':'staying with first',
# #     'list':{
# #         'firstcmd':[
# #             'first',
# #             'first2',
# #         ]
# #     }
# # }
# # dct2 = {
# #     'main':'second',
# #     'more':'adding from second',
# #     'list':{
# #         'seccondcmd':[
# #             'second',
# #             'second2',
# #         ]
# #     }
# # }

# with open('default_notebookrc.yml') as ycf:
#     dct1 = yaml.load(ycf, Loader=yaml.FullLoader)
# with open('/home/acobb/.notebookrc') as ycf:
#     dct2 = yaml.load(ycf, Loader=yaml.FullLoader)


# print(json.dumps(dct1, indent=4))
# print(json.dumps(dct2, indent=4))

# print(json.dumps(update_config(dct1, dct2), indent=4))
