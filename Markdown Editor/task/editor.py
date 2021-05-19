# region Variables
available_formatters = ("plain",
                        "bold",
                        "italic",
                        "header",
                        "link",
                        "inline-code",
                        "ordered-list",
                        "unordered-list",
                        "new-line")
special_commands = ("!help", "!done")
result = ""
formatter = ""
# endregion

# region Methods


def __help__():
    output_for_available_formatters = ""
    for available_formatter in available_formatters:
        output_for_available_formatters += available_formatter + " "
    print("Available formatters:", output_for_available_formatters)

    output_for_special_commands = ""
    for special_command in special_commands:
        output_for_special_commands += special_command + " "
    print("Special commands:", output_for_special_commands)
    
    
def plain():
    global result
    result += input_text()


def bold():
    global result
    result += "**" + input_text() + "**"


def italic():
    global result
    result += "*" + input_text() + "*"


def link():
    global result
    label = input("Label:")
    url = input("URL:")
    result += "[" + label + "]" + "(" + url + ")"


def inline_code():
    global result
    result += "`" + input_text() + "`"


def header():
    global result
    level = int(input("Level:"))
    if level < 1 or level > 6:
        print("The level should be within the range of 1 to 6")
        return
    text = input_text()
    result += "#" * level + " " + text + "\n"


def new_line():
    global result
    result += "\n"
    return


def __list__(list_type):
    global result
    num_of_rows = 0

    while num_of_rows < 1:
        num_of_rows = int(input("Number of rows:"))
        if num_of_rows < 1:
            print("The number of rows should be greater than zero")
        if num_of_rows == "!done":
            __exit__()

    for num_of_row in range(1, num_of_rows + 1):
        if list_type == "ordered-list":
            result += f"{num_of_row}. "
        elif list_type == "unordered-list":
            result += "* "
        result += input(f"Row #{num_of_row}") + "\n"


def input_text():
    return input("Text:")


def __exit__():
    exit()

# endregion


# region Main()

while formatter != "!done":
    formatter = input("Choose a formatter:")
    # check the formatter is valid
    if formatter in available_formatters or formatter in special_commands:
        if formatter == "!done":
            __exit__()
        elif formatter == "!help":
            __help__()
        elif formatter == "plain":
            plain()
        elif formatter == "bold":
            bold()
        elif formatter == "italic":
            italic()
        elif formatter == "header":
            header()
        elif formatter == "link":
            link()
        elif formatter == "inline-code":
            inline_code()
        elif formatter == "new-line":
            new_line()
        elif formatter == "ordered-list" or formatter == "unordered-list":
            __list__(formatter)
        print(result)
    else:
        print("Unknown formatting type or command")
# endregion
