

import json
import datetime
import uuid
import argparse
import re

print('starting')

# Argparse
aparse = argparse.ArgumentParser(description='Task Warrior TMUX wrapper')
# Input
aparse.add_argument('-i', '--input',          action='append', default=[], help='')
aparse.add_argument('-p', '--python',         action='store_true', help='')
aparse.add_argument('-r', '--ruby',           action='store_true', help='')
aparse.add_argument('-j', '--json',           action='store_true', help='')
aparse.add_argument('-f', '--from-clipboard', action='store_true', help='')
aparse.add_argument('-t', '--to-clipboard',   action='store_true', help='')

args = aparse.parse_args()
print(args)

class MasterJSONParser:
    def _parse_json(self, obj):
        json.loads(obj)
        pass

    def _parse_object(self, obj):
        pass


class Deconstructor2000:

    def __init__(self):
        self.x = 1

    def parse_entity(self, input_obj):
        print(f"\n---\n parsing: {input_obj}\n")
        obj_format = None
        print(self.data_type(input_obj))


        # is_dict = re.search(r'^{(.*)}$', input_obj)
        # is_list = re.search(r'^\[(.*)]$', input_obj)
        # is_kv   = re.search(data_object, input_obj)
        # is_kv   = re.search(f"({data_object} *(:|=|=>) *{data_object})", input_obj)

        # if is_dict is not None:
        #     print('is dict')
        #     regex = is_dict
        #     obj_format = 'dict'
        # elif is_list is not None:
        #     print('is list')
        #     regex = is_list
        #     obj_format = 'list'
        # elif is_kv is not None:
        #     # print('is kv')
        #     regex = is_kv
        #     obj_format = 'kv'
        # else:
        #     print('is nada')
        #     regex = False
        #     obj_format = 'value'

        # if obj_format == 'dict':
        #     print(regex.group(1))
        #     # print(f"{data_object} *(:|=|=>)? *{data_object},*")
        #     # sets = re.findall(f"{data_object} *(:|=|=>)? *({data_object}|{data_object} *(:|=|=>) *(\[|\{)({data_object}(,|:|=|=>)? *)*(]|})),*", regex.group(1))
        #     # print(sets)
        #     # for i in sets:
        #     #     print(i)
        #     # # i = 0
        #     # # while sets:
        #     # #     print(i)
        #     # #     try:
        #     # #         print(f"  -{sets.group(i)}-")
        #     # #     except IndexError:
        #     # #         break
        #     # #     i += 1
        # elif obj_format == 'kv':
        #     key = regex.group(2)[1:-1]
        #     value = regex.group(4)
        #     if value.startswith('"') or value.startswith("'"):
        #         value = value[1:-1]
        #     try:
        #         if '.' in value:
        #             value = float(value)
        #         else:
        #             value = int(value)
        #     except ValueError:
        #         pass
        #     if value in ['None', 'null', 'nil']:
        #         value = None
        #     kv = {key: value}
        #     print(f"kv return: {kv}")
        #     return kv

        # # i = 1
        # # while regex:
        # #     try:
        # #         print(f"  {regex.group(i)}")
        # #     except IndexError:
        # #         break
        # #     i += 1

    def data_type(self, input_obj):
        # print(f"\n---\n parsing: {input_obj}")
        """
        This just determines what type of data format was given
        """
        # Text data
        input_obj.strip()
        single_tick_value = r'\'[a-zA-Z0-9`~!@#$%^&*()-_=+[\]{}\. "]*\''
        double_tick_value = r'"[a-zA-Z0-9`~!@#$%^&*()-_=+[\]{}\. \']*"'
        numeric_value = r'[0-9]+\.?[0-9]*'
        kv_seporator = r' *(:|=|=>) *'
        python_object = r'(\'|")?(([a-zA-Z0-9]*\.)*[a-zA-Z0-9]*\([a-zA-z0-9`~!@#$%^&*-_=+\[\]\{\};:\'",\. ]*\))(\'|")?'

        value_object = f"({single_tick_value}|{double_tick_value}|{numeric_value}|{python_object}|None|nil|null)"
        data_object = value_object
        intermediate_list_object = f"\[( *{data_object} *,?)*]"
        intermediate_kv_object = f"({data_object}{kv_seporator}{data_object})"
        intermediate_dict_object = f"{{({intermediate_kv_object} *,? *)*}}"
        intermediate_data_objects = f"( *({intermediate_dict_object}|{intermediate_kv_object}|{intermediate_list_object}|{data_object}) *,?)"
        list_object = f"^\[( *({intermediate_data_objects}) *,?)*]$"
        kv_object = f"^{intermediate_kv_object}$"
        dict_kv_objects = f"({intermediate_data_objects}{kv_seporator}{intermediate_data_objects})"
        list_objects = f" *({intermediate_data_objects}) *,?"
        dict_object = f"^{{( *({data_object}{kv_seporator}({intermediate_data_objects})) *,?)*}}$"

        # Class or Object data
        # datetime_object = r'(\'|")?((datetime\.(datetime|timedelta|tzinfo|timezone|date|time)\(.*\)))(\'|")?'
        # datetime_object = r'(datetime)'

        # print(f"single_tick_value: {single_tick_value}")
        # print(f"double_tick_value: {double_tick_value}")
        # print(f"numeric_value: {numeric_value}")
        # print(f"kv_seporator: {kv_seporator}")
        # print(f"value_object: {value_object}")
        # print(f"data_object: {data_object}")
        # print(f"intermediate_list_object: {intermediate_list_object}")
        # print(f"intermediate_kv_object: {intermediate_kv_object}")
        # print(f"intermediate_dict_object: {intermediate_dict_object}")
        # print(f"intermediate_data_objects: {intermediate_data_objects}")
        # print(f"list_object: {list_object}")
        # print(f"kv_object: {kv_object}")
        # print(f"dict_object: {dict_object}")

        if re.search(dict_object, input_obj):
            return_obj = {}
            for r in re.findall(dict_kv_objects, input_obj[1:-1]):
                i = 0
                for q in r:
                    if q == '':
                        continue
                    i += 1
                    if i == 3:
                        key = q
                    if i == 6:
                        value = q
                # print(f"Answer: -{key}- : -{value}-")
                # print(self.data_type(key))
                # print(self.data_type(value))
                key = self.data_type(key)
                value = self.data_type(value)
                # print(f"key: {key}, {type(key)}")
                # print(f"value: {value}, {type(value)}")
                return_obj[key] = value
        elif re.search(list_object, input_obj):
            return_obj = []
            for r in re.findall(list_objects, input_obj[1:-1]):
                # print(r)
                i = 0
                for q in r:
                    if q == '':
                        continue
                    i += 1
                    # print(f"    {q}")
                    if i == 2:
                        item = q
                item = self.data_type(item)
                # print(f"Item: {item}")
                return_obj.append(item)

        elif re.search(python_object, input_obj):
            input_obj = input_obj.strip()
            if input_obj.endswith(','):
                input_obj = input_obj[:-1]
            input_obj = input_obj.strip()
            if input_obj.startswith(('"',"'")):
                    input_obj = input_obj[1:-1]
            match = re.match(python_object, input_obj).group(2)
            if args.python:
                if match.startswith('datetime'):
                    obj = eval(match)
                elif match.startswith('UUID'):
                    obj = uuid.UUID(match[6:-2])
            else:
                obj = str(match)
            return_obj = obj
        else:
            input_obj = input_obj.strip()
            if input_obj.endswith(','):
                input_obj = input_obj[:-1]
            input_obj = input_obj.strip()
            if input_obj.startswith(('"',"'")):
                    input_obj = input_obj[1:-1]
            else:
                # print(f"-{input_obj}-")
                try:
                    if '.' in input_obj:
                        input_obj = float(input_obj)
                    else:
                        input_obj = int(input_obj)
                except ValueError:
                    if input_obj in ['None', 'nil', 'null']:
                        input_obj = None
                # print(type(input_obj))

            return_obj = input_obj
            print('is nada')

        return return_obj

mp = MasterJSONParser()
d2 = Deconstructor2000()

# # Good data
d2.parse_entity(str({'some':'dict'}))
d2.parse_entity(str(['list', 'items']))
d2.parse_entity("'key':'value'")
d2.parse_entity('value')
d2.parse_entity('123456')
d2.parse_entity('123.456')
d2.parse_entity('None')
d2.parse_entity('nil')
# Complex data
d2.parse_entity("{'some':'dict', 'that'='keeps',\"going\"='for'   ,   'a' =>    'while'}")
d2.parse_entity("{'some':'dict', 'that'='keeps',\"going\"='for\"\"'   ,   'a' =>    'while'}")
d2.parse_entity("{'one':'1', 'two':2, 'three':{'five':'5', 'six':6}, 'four':[1,2,'a','c']}")
d2.parse_entity(str(['list', 'items','like',    'a'  ,'lot']))
d2.parse_entity("{'five':'5', 'six':'6'}")
d2.parse_entity("['str', 123, None, {'five':'5', 'six':'6'}, [1,2,'a','c']]")
d2.parse_entity("['str', 123, None, {'five':'5', 'six':6}, [1,2,'a','c']]")
d2.parse_entity("'key':'value, tahst keeps goidnasf\''")

# Classes and objects
d2.parse_entity('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)')
d2.parse_entity("'datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)'")
d2.parse_entity(' datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)')
d2.parse_entity('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333) ')
d2.parse_entity(' datetime.datetime(2022, 1, 20, 14, 5, 47, 943333) ')
d2.parse_entity('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333), ')
d2.parse_entity('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333) ,')
d2.parse_entity('datetime.timedelta(seconds=3600)')
d2.parse_entity("UUID('00ac46e5-67f2-4228-898c-b21910876f66')")
# uuid.uuid4()

# Even more complex
d2.parse_entity("{'time': 'datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)'}")
d2.parse_entity("[datetime.datetime(2022, 1, 20, 14, 5, 47, 943333), datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)]")

# Bad data
d2.parse_entity("{'some':")



for i in args.input:
    # print(i)
    # print(mp._parse_json(i))
    # d2.parse_entity(i)
    d2.parse_entity(i)

print('ending')

# py rough_json_parser.py -i "{'some':'dict', \"another\":'item', 'Final'=>'thing','list':[1,2,'three','$'], 'more':'dict'}" -i "['some':'dict', \"another\":'item', 'Final'=>'thing','list':[1,2,'three','$']]" -i "'some':'some'" -i '"some"     =>"thing"' -i "'some':123" -i "'some':None" 