import numpy as np

def collect_info(array):
    shape = array.shape
    num_of_dim = array.ndim
    length = len(array)
    size = array.size
    return f"Shape: {shape}; dimensions: {num_of_dim}; length: {length}; size: {size}"
