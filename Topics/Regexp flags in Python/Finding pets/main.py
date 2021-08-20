import re 

pets = input()
# your code here
pattern = r"(dog|cat|parrot|hamster)"
res = re.findall(pattern, pets, flags=re.I)
print(res)
