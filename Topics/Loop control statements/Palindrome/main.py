word = input()
i = len(word) // 2
is_palindrome = False

for pos in range(i):
    if word[pos] != word[-1 - pos]:
        break
else:
    is_palindrome = True

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
