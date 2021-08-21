def check_name(variable_name):
    not_allowed_start_symbols = ['l', 'I', 'O']
    if variable_name in not_allowed_start_symbols:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
        return

    if variable_name.islower():
        print("It is a common variable")
    elif variable_name.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
