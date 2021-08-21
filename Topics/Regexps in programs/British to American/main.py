import re

string = input()
# your code here
pattern = "(?<=[A-z])ou"

res = re.sub(pattern, "o", string)
print(res)
