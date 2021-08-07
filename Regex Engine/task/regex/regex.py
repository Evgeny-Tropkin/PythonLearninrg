def parse_reg_ex(reg_ex_string):
    """The method accepts a string containing a Regular Expression.
       Returns a list of tokens which were found in the entered regular expression """
    special_characters = ('.', )
    res = []
    substring = []

    if len(reg_ex_string) != 0:
        for pos, char in enumerate(reg_ex_string):
            if pos == 0 and char == '^':
                res.append(char)
                continue
            if char in special_characters:
                if len(substring) != 0:
                    res.append(''.join(substring))
                    substring.clear()
                res.append(char)
                continue
            if pos == len(reg_ex_string) - 1 and char == '$':
                continue
            substring.append(char)
        if len(substring) > 0:
            res.append(''.join(substring))
        substring.clear()
        if reg_ex_string[-1] == '$':
            res.append('$')

    return res


def process_string(processed_string, reg_ex_list):
    """The method accepts:
        - A regular expression as a list of tokens
        - A string that will be matched against a regular expression
       Returns the result of matching"""
    res = [False]

    if len(reg_ex_list) == 0:
        res[0] = True
    elif len(processed_string) == 0:
        pass
    else:
        res[0] = match(processed_string, reg_ex_list, is_startswith=reg_ex_list[0] == '^')

    return all(res)


def match(processed_string, reg_ex_list, is_startswith=False, is_endswith=False):
    res = False
    checking_char_index = 0
    current_lex_pos = 0
    if is_startswith:
        current_lex_pos = 1
    if is_endswith:
        pass
    while current_lex_pos < len(reg_ex_list):
        target_item = reg_ex_list[current_lex_pos]
        if target_item == '.':
            if not processed_string[checking_char_index].isspace():
                checking_char_index += 1
                current_lex_pos += 1
                continue

        if processed_string.startswith(target_item, checking_char_index):
            checking_char_index += len(target_item)
            current_lex_pos += 1
        else:
            if is_startswith:
                break
            checking_char_index += 1
            current_lex_pos = 0

        if checking_char_index >= len(processed_string) and current_lex_pos < len(reg_ex_list):
            break
    else:
        res = True

    return res


def main():
    reg_ex, processed_string = input().split('|')

    parsed_reg_ex = parse_reg_ex(reg_ex)

    print(process_string(processed_string, parsed_reg_ex))


# region Script
if __name__ == "__main__":
    main()
# endregion
