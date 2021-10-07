import re

string = input()
# your code here
pattern = "Good (morning|afternoon|evening)"

res = re.match(pattern, string, flags=re.I)
if res:
    print(res.group())
else:
    print("No greeting!")
