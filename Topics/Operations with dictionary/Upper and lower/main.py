# the list with words from string
# please, do not modify it
some_iterable = input().split()

new_dict = {word.upper(): word.lower() for word in some_iterable}
print(new_dict)
