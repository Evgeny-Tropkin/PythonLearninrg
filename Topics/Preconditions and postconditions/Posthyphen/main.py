import re

string = input()
# your code here
pattern = r"(?<=-)\w+"
res = re.search(pattern, string)
if res:
    print(res.group())
