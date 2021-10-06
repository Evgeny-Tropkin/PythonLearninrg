import numpy as np


def custom_sum(arg1, arg2):
    arg1_is_list = type(arg1) is list
    arg2_is_list = type(arg2) is list
    if arg1_is_list and arg2_is_list:
        return "Both arguments are lists, not arrays"
    elif arg1_is_list or arg2_is_list:
        return "One argument is a list"
    else:
        arg1_is_array = type(arg1) is np.ndarray
        arg2_is_array = type(arg2) is np.ndarray
        if arg1_is_array and arg2_is_array:
            return arg1 + arg2
