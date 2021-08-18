import re

template = r'are you ready??.?.?'
string = input()
match = re.match(template, string)
if match:
    print(len(match.group()))
else:
    print('0')
