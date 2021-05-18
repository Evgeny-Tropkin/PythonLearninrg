def find_my_list(lists, my_list):
    for i, lst in enumerate(lists):
        if lst is my_list:
            return i

    return None
