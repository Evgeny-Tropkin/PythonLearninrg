import re       


names = input()
# your code here
res = re.split(r"\d+", names)
print(res)
