import re

string = input()
# your code here
capitalized_words_pattern = r"(?<!\w)[A-Z][A-z]*"
digits_pattern = r"[\d]+"

capitalized_words = re.findall(capitalized_words_pattern, string)
digits = re.findall(digits_pattern, string)

print("Capitalized words:", ", ".join(capitalized_words))
print("Digits:", ", ".join(digits))
