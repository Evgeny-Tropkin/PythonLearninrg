import re


string = input()
pattern = "happy"
match = re.findall(pattern, string)
print(len(match))
