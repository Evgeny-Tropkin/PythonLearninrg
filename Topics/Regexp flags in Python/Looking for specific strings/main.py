import re

string = input()
# your code here
pattern = r"b.*l$"
match = re.match(pattern, string, flags=re.I | re.S)
if match:
    print(match.group())
else:
    print("No match")
