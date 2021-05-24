input_str = input().lower().split(" ")
result = {word: input_str.count(word) for word in input_str}

for k, v in result.items():
    print(f"{k} {v}")
