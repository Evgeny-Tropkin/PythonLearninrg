input_str = input().split(" ")
result = {word.lower(): 0 for word in input_str}

for word in input_str:
    result[word.lower()] += 1

for k, v in result.items():
    print(f"{k} {v}")
