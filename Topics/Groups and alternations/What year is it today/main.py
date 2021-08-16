import re


# put your regex in the variable template
template = r"(\d\d?[\./]){2}(\d{4})"
string = input()
# compare the string and the template
match = re.match(template, string)
if match is None:
    print(match)
else:
    print(match.group(2))
