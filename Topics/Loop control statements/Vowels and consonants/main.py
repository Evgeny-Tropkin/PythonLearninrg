inp_str = input()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxz"

for char in inp_str:
    if char in vowels:
        print("vowel")
    elif char in consonants:
        print("consonant")
    else:
        break
