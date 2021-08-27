string = input()
sub_string = "old"

forward_search_index = string.find(sub_string)
backward_search_index = string.rfind(sub_string)
if backward_search_index > forward_search_index:
    print(backward_search_index)
else:
    print(forward_search_index)
