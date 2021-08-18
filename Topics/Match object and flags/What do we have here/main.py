import re

template = r'... Jude'
string = input()
match = re.match(template, string)
print(match and match.group())
