lower_case_words = input().split()

mixed_case_identifier = lower_case_words[0]
mixed_case_identifier += ''.join([word.capitalize() for word in lower_case_words[1::]])

print(mixed_case_identifier)
