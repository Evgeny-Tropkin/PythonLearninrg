word_in_camel_case = input()
result = word_in_camel_case[0].lower()

for char_num in range(1, len(word_in_camel_case)):
    if word_in_camel_case[char_num].isupper():
        result += "_"
    result += word_in_camel_case[char_num].lower()

print(result)
