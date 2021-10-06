import numpy as np


def custom_sum(arg1, arg2):
    res = ''
    arg1_is_list = isinstance(arg1, list)
    arg2_is_list = isinstance(arg2, list)
    if arg1_is_list and arg2_is_list:
        res = "Both arguments are lists, not arrays"
    elif arg1_is_list or arg2_is_list:
        res = "One argument is a list"
    else:
        arg1_is_array = isinstance(arg1, np.ndarray)
        arg2_is_array = isinstance(arg2, np.ndarray)
        if arg1_is_array and arg2_is_array:
            res = arg1 + arg2

    return res
