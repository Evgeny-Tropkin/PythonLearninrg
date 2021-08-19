import re


string = input()
# your code
pattern = re.compile(r"@\w+")
string_1 = pattern.sub("<AUTHOR>", string, 1)
res = pattern.sub("<HANDLE>", string_1)

print(res)
