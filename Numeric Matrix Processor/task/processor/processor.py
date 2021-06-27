# region Classes
class CustomMatrix:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.set_value()

    def get_rows_count(self):
        return self.__rows

    def get_columns_count(self):
        return self.__columns

    def set_value(self):
        pass

    def __add__(self, other):
        if other.get_rows() == self.__rows and other.get_columns() == self.__columns:
            pass

# end region

# region Methods
def main():
    matrix1 = input_matrix()
    matrix2 = input_matrix()
    try:
        result = matrix1 + matrix2
    except ValueError:
        print("ERROR")
    else:
        print(result)


def input_matrix():
    """ The function is intended for entering a matrix of a given dimension. \n
        Returns a List with elements of the List type. \n
        The number of nesting levels depends on the specified dimension of the matrix"""
    return []
# endregion


# region Script
if __name__ == "__main__":
    main()
# end region
