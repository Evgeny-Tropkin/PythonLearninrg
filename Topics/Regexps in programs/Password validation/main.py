import re

password = input()
# your code here
pattern = "[A-z0-9]{6,15}"

res = re.match(pattern, password, flags=re.ASCII)
if res:
    print("Thank you!")
else:
    print("Error!")
