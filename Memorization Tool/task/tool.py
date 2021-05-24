menu = {"1": {"title": "Add flashcards", "1": {"title": "Add new flashcard"}, "2": {"title": "Exit"}},
        "2": {"title": "Practice flashcards"},
        "3": {"title": "Exit"}}
menu_path = []
current_menu_level = menu


# region Methods
def show_menu(menu_dict):
    for menu_item in menu_dict.keys():
        if menu_item == "title":
            continue
        print(f"{menu_item}. {menu_dict[menu_item]['title']}")


def select_menu_item(menu_dict):
    while True:
        selected_item_number = input()
        if selected_item_number in menu_dict.keys():
            return selected_item_number
        else:
            print(f"{selected_item_number} is not an option")


def execute_selected_item(menu_dict, item):
    global current_menu_level
    if menu_dict[item]['title'] == "Exit":
        if len(menu_path) > 0:
            current_menu_level = menu_path.pop()
        else:
            __exit__()


def add_flashcards():
    pass


def __exit__():
    print("Bye!")
    exit()
# endregion


# region Main()
while True:
    show_menu(current_menu_level)
    selected_menu_item = select_menu_item(current_menu_level)
    if len(current_menu_level[selected_menu_item]) > 1:
        menu_path.append(current_menu_level)
        current_menu_level = current_menu_level[selected_menu_item]
        continue
    execute_selected_item(current_menu_level, selected_menu_item)
# endregion
