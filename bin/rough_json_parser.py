

import json
import datetime
import uuid
import argparse
import re

# Argparse
aparse = argparse.ArgumentParser(description='Task Warrior TMUX wrapper')
# Input
aparse.add_argument('-i', '--input',          action='append', default=[], help='input string to parse')
aparse.add_argument('-p', '--python',         action='store_true', help='return a python dict')
aparse.add_argument('-r', '--ruby',           action='store_true', help='return a ruby hash')
aparse.add_argument('-j', '--json',           action='store_true', help='return a json object')
aparse.add_argument('-f', '--from-clipboard', action='store_true', help='use the clipboard (not implemented)')
aparse.add_argument('-t', '--to-clipboard',   action='store_true', help='export to clipboard (not implemented)')

args = aparse.parse_args()

# class MasterJSONParser:
#     def _parse_json(self, obj):
#         json.loads(obj)
#         pass

#     def _parse_object(self, obj):
#         pass


class Deconstructor2000:

    def __init__(self, indent=2):
        self.indent = indent

    def parse_thing(self, input_obj):
        # print(f"\n---\n parsing: {input_obj}\n")
        obj = self._object_parser(input_obj)
        # print(args)
        if args.json:
            print(json.dumps(obj, indent=self.indent))
            return json.dumps(obj, indent=self.indent)
        elif args.python:
            # print(json.dumps(obj, indent=self.indent))
            return obj
        elif args.ruby:
            str_obj = json.dumps(obj)
            str_obj = str_obj.replace('": ', '" => ')
            print(str_obj)
            return str_obj


    def _object_parser(self, input_obj):
        """
        Given a string, this will return a properly formatted data type
            given "{'one':'1', 'two':2}" it will return {'one':'1', 'two':2}
            given "['one', 2, 2.3, ]" it will return ['one', 2, 2.3]
        """
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
                key = self._object_parser(key)
                value = self._object_parser(value)
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
                    if i == 2:
                        item = q
                item = self._object_parser(item)
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
                try:
                    if '.' in input_obj:
                        input_obj = float(input_obj)
                    else:
                        input_obj = int(input_obj)
                except ValueError:
                    if input_obj in ['None', 'nil', 'null']:
                        input_obj = None

            return_obj = input_obj

        return return_obj

# mp = MasterJSONParser()
d2 = Deconstructor2000()
for i in args.input:
    d2.parse_thing(i)

# # Good data
# d2.parse_thing(str({'some':'dict'}))
# d2.parse_thing(str(['list', 'items']))
# d2.parse_thing("'key':'value'")
# d2.parse_thing('value')
# d2.parse_thing('123456')
# d2.parse_thing('123.456')
# d2.parse_thing('None')
# d2.parse_thing('nil')
# # Complex data
# d2.parse_thing("{'some':'dict', 'that'='keeps',\"going\"='for'   ,   'a' =>    'while'}")
# d2.parse_thing("{'some':'dict', 'that'='keeps',\"going\"='for\"\"'   ,   'a' =>    'while'}")
# d2.parse_thing("{'one':'1', 'two':2, 'three':{'five':'5', 'six':6}, 'four':[1,2,'a','c']}")
# d2.parse_thing(str(['list', 'items','like',    'a'  ,'lot']))
# d2.parse_thing("{'five':'5', 'six':'6'}")
# d2.parse_thing("['str', 123, None, {'five':'5', 'six':'6'}, [1,2,'a','c']]")
# d2.parse_thing("['str', 123, None, {'five':'5', 'six':6}, [1,2,'a','c']]")
# d2.parse_thing("'key':'value, tahst keeps goidnasf\''")

# # Classes and objects
# d2.parse_thing('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)')
# d2.parse_thing("'datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)'")
# d2.parse_thing(' datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)')
# d2.parse_thing('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333) ')
# d2.parse_thing(' datetime.datetime(2022, 1, 20, 14, 5, 47, 943333) ')
# d2.parse_thing('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333), ')
# d2.parse_thing('datetime.datetime(2022, 1, 20, 14, 5, 47, 943333) ,')
# d2.parse_thing('datetime.timedelta(seconds=3600)')
# d2.parse_thing("UUID('00ac46e5-67f2-4228-898c-b21910876f66')")
# # uuid.uuid4()

# # Even more complex
# d2.parse_thing("{'time': 'datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)'}")
# d2.parse_thing("[datetime.datetime(2022, 1, 20, 14, 5, 47, 943333), datetime.datetime(2022, 1, 20, 14, 5, 47, 943333)]")

# # Bad data
# d2.parse_thing("{'some':")
