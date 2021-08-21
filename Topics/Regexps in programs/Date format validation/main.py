import re

string = input()
# your code here
pattern = r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/[\d]{4}"

match = re.match(pattern, string)
print(bool(match))
