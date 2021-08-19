import re

string = input()
# your code
pattern = r"<START>|<END>"
divided = re.split(pattern, string)
print(divided[1])
