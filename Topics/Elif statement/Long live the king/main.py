column = int(input())
row = int(input())

num_of_possible_directions = None
is_row_in_middle = row in range(2, 8)
is_column_in_middle = column in range(2, 8)

if is_column_in_middle and is_row_in_middle:
    #  point in middle
    num_of_possible_directions = 8
else:
    if is_column_in_middle or is_row_in_middle:
        #  point on a side
        num_of_possible_directions = 5
    else:
        # point in a corner
        num_of_possible_directions = 3

print(num_of_possible_directions)
