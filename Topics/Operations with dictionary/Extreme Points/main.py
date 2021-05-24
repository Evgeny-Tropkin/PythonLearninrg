# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
any_key = list(test_dict.keys())[0]
max_value_key = any_key
max_value = test_dict[max_value_key]
min_value_key = any_key
min_value = test_dict[min_value_key]

for key, value in test_dict.items():
    if value > max_value:
        max_value = value
        max_value_key = key
    elif value < min_value:
        min_value = value
        min_value_key = key

print(f"min: {min_value_key}")
print(f"max: {max_value_key}")
