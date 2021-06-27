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
    return []
# endregion


# region Script
if __name__ == "__main__":
    main()
# end region
