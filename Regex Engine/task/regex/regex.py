def parse_reg_ex(reg_ex_string):
    """The method accepts a string containing a Regular Expression.
       Returns a list of tokens which were found in the entered regular expression """
    res = []

    return res


def process_string(processed_string, reg_ex_list):
    """The method accepts:
        - A regular expression as a list of tokens
        - A string that will be matched against a regular expression
       Returns the result of matching"""
    res = None

    return res


def main():
    user_input = input().split('|')

    reg_ex = user_input[0]
    processed_string = user_input[1]

    parsed_reg_ex = parse_reg_ex(reg_ex)

    print(process_string(processed_string, parsed_reg_ex))


# region Script
if __name__ == "__main__":
    main()
# endregion
