import re

string = input()
# your code here
pattern = r"(?<=\$)(\d+)"
expenses = re.findall(pattern, string)
s = 0
for expense in expenses:
    s += int(expense)
print(f"This week you have spent: {s} dollars")
