import re

# your code here
word = input()
pattern = r"\w+-\w+"

print(bool(re.match(pattern, word)))
