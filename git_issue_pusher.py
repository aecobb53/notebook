import requests

owner = 'aecobb53'
repo = 'notebook'
url = f"http://repos/{owner}/{repo}/issues/1"

arguments = {
    'title':'example issue for testing'
}
arguments = {
  "title": "Found a bug",
  "body": "I'm having a problem with this.",
  "assignees": [
    "octocat"
  ],
  "milestone": 1,
  "labels": [
    "bug"
  ]
}
arguments = {}

print(f"url: {url},  args:{arguments}")
if arguments == {}:
    print('running without arguments')
    response = requests.get(url)
else:
    print('running with arguments')
    response = requests.get(url, arguments)

print(response)
print(response.status_code)

exit()
try:
    print(response.json())
except:
    print('there is no json data received')

# arguments = {
#     'title':'example issue for testing'
# }
# arguments = {
#   "title": "Found a bug",
#   "body": "I'm having a problem with this.",
#   "assignees": [
#     "octocat"
#   ],
#   "milestone": 1,
#   "labels": [
#     "bug"
#   ]
# }


# print(f"url: {url},  args:{arguments}")
# if arguments == {}:
#     print('running without arguments')
#     response = requests.post(url)
# else:
#     print('running with arguments')
#     response = requests.post(url, arguments)

# print(response)
# print(response.status_code)

# exit()
# try:
#     print(response.json())
# except:
#     print('there is no json data received')
