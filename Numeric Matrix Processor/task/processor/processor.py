# region Classes
class CustomMatrix:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__value = [[0 for _ in range(self.__columns)] for _ in range(self.__rows)]

    def get_rows_count(self):
        return self.__rows

    def get_columns_count(self):
        return self.__columns

    def get_value(self):
        return self.__value

    def set_value(self, other):
        self.__value = other.get_value()

    def get_row(self, row_num):
        return self.__value[row_num - 1]

    def set_row(self, row_num, row):
        self.__value[row_num - 1] = row

    def append_row(self, row_list):
        self.__value.append(row_list)

    def get_column(self, col_num):
        return [row[col_num - 1] for row in self.__value]

    def get_cell_value(self, row_num, col_num):
        return self.__value[row_num - 1][col_num - 1]
        # TODO: implement checking of "the value out of range":
        #  for row_num outside the range (cells.__rows)
        #  for col_num outside the range (self.__columns).
        #  If the check is not passed, return IndexError

    def set_cell_value(self, row_num, col_num, value):
        self.__value[row_num - 1][col_num - 1] = value
        # TODO: implement checking of "the value out of range":
        #  for row_num outside the range (cells.__rows)
        #  for col_num outside the range (self.__columns).
        #  If the check is not passed, return IndexError

    def multiple_by_number(self, num):
        res = CustomMatrix(self.__rows, self.__columns)
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__columns + 1):
                res.set_cell_value(row, col, self.get_cell_value(row, col) * num)
        return res

    def multiple(self, other):
        """Multiplication of matrices"""
        if self.__columns == other.get_rows_count:
            res_rows_count = self.__rows
            res_columns_count = other.get_columns_count()
            res = CustomMatrix(res_rows_count, res_columns_count)
            for i in range(1, res_rows_count + 1):
                row = self.get_row(i)
                column = other.get_column(i)
                res_row_i = [row[pos] * column[pos] for pos in range(res_columns_count)]

                res.set_row(i, res_row_i)
                
        else:
            raise ValueError

    def __add__(self, other):
        """Addition of matrices"""
        if other.get_rows_count() == self.__rows and other.get_columns_count() == self.__columns:
            res = CustomMatrix(self.__rows, self.__columns)
            for row in range(1, self.__rows + 1):
                for column in range(1, self.__columns + 1):
                    new_matrix_cell_value = self.get_cell_value(row, column) + other.get_cell_value(row, column)
                    res.set_cell_value(row, column, new_matrix_cell_value)
            return res
        else:
            raise ValueError

    def __mul__(self, other):
        if type(other) == int:
            return self.multiple_by_number(other)
        elif type(other) == CustomMatrix:
            return self.multiple(other)
        else:
            raise TypeError

    def __repr__(self):
        for row in self.__value:
            print(' '.join(map(str, row)))
        return ''

# end region


# region Methods
def main():
    matrix1 = input_matrix()
    num = int(input())
    try:
        result = matrix1 * num
    except TypeError:
        print("ERROR")
    else:
        print(result.__repr__())


def input_matrix():
    """ The function is intended for entering a matrix of a given dimension. \n
        Returns an object of CustomMatrix type"""
    size = input().split()
    rows = int(size[0])
    columns = int(size[1])
    res = CustomMatrix(rows, columns)

    for i in range(1, rows + 1):
        row = [int(item) for item in input().split()]
        res.set_row(i, row)

    return res
# endregion


# region Script
if __name__ == "__main__":
    main()
# end region
