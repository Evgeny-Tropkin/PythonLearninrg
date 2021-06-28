import MenuItem as processorMenu


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
    current_menu_level = create_menu()

    while True:
        show_menu(current_menu_level)
        selected_item = select_menu_item(current_menu_level)
        execute_selected_item(selected_item)


def create_menu():
    root = processorMenu.MenuItem(None, "root", "Main menu", False)
    # region Main menu
    # region item_1 ("Add matrices" menu)
    item_1 = processorMenu.MenuItem(root, "1", "1. Add matrices", True)
    # endregion
    # region item_2 ("Multiply matrix by a constant" menu)
    item_2 = processorMenu.MenuItem(root, "2", "2. Multiply matrix by a constant", True)
    # endregion
    # region item_3 ("Multiply matrices" menu)
    item_3 = processorMenu.MenuItem(root, "3", "3. Multiply matrices", True)
    # endregion
    # region item_0
    item_0 = processorMenu.MenuItem(root, "0", "0. Exit", True)
    # endregion

    # region Menu relations
    root.set_nodes(item_1, item_2, item_3, item_0)
    # endregion

    return root


def show_menu(menu_item):
    menu_item_nodes = menu_item.get_nodes().values()
    for node in menu_item_nodes:
        print(node.get_title())


def select_menu_item(menu_item):
    while True:
        selected_item = input("Your choice: ")
        if selected_item in menu_item.get_nodes().keys():
            nodes = menu_item.get_nodes()
            return nodes[selected_item]
        else:
            print(f"{selected_item} is not an option")
            return menu_item


def execute_selected_item(menu_item):
    menu_id = menu_item.get_id()

    if menu_id == "0":
        __exit__()
    if menu_id == "1":
        matrix1 = input_matrix("first matrix")
        matrix2 = input_matrix("second matrix")
        try:
            result = matrix1 + matrix2
        except ValueError:
            print("ERROR")
        else:
            print("The result is:")
            print(result.__repr__())

    elif menu_id == "2":
        matrix1 = input_matrix("matrix")
        num = int(input())
        try:
            result = matrix1 * num
        except TypeError:
            print("ERROR")
        else:
            print("The result is:")
            print(result.__repr__())

    elif menu_id == "3":
        matrix1 = input_matrix("first matrix")
        matrix2 = input_matrix("second matrix")
        try:
            result = matrix1 * matrix2
        except ValueError:
            print("ERROR")
        else:
            print("The result is:")
            print(result.__repr__())


def input_matrix(part_of_message):
    """ The function is intended for entering a matrix of a given dimension. \n
        Accepts a part of the message to prompt the user
        Returns an object of CustomMatrix type"""
    size = input(f"Enter size of {part_of_message}: ").split()
    rows = int(size[0])
    columns = int(size[1])
    res = CustomMatrix(rows, columns)

    print(f"Enter {part_of_message}: ")

    for i in range(1, rows + 1):
        row = [float(item) for item in input().split()]
        res.set_row(i, row)

    return res


def __exit__():
    print("Bye!")
    exit()
# endregion


# region Script
if __name__ == "__main__":
    main()
# endregion
