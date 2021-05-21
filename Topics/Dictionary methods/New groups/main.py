# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
number_of_groups = int(input())
groups_data = dict.fromkeys(groups)

for i in range(number_of_groups):
    number_of_children = int(input())
    groups_data[groups[i]] = number_of_children

print(groups_data)
