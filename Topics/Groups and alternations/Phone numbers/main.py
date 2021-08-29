import re

string = input()
# your code here
pattern = r"^\+(\d{1})[ -]?(\d{3})[ -]?((\d[ -]?){7})"
res = re.search(pattern, string)
if res:
    print("Full number: ", res.group(), "")
    print("Country code: ", res.groups()[0], "")
    print("Area code: ", res.groups()[1], "")
    print("Number: ", res.groups()[2])
else:
    print("No match")
