text = input()
words = text.split()
for word in words:
    if word.lower().startswith(("https://", "http://", "www.")):
        print(word)
