def list_sum(some_list):
    if some_list == []:
        return 0
    elif len(some_list) == 1:
        return some_list[0]
    else:
        return list_sum(some_list[:-1]) + some_list[-1]
