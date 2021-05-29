menu = {"1": {"title": "Add flashcards", "1": {"title": "Add a new flashcard"}, "2": {"title": "Exit"}},
        "2": {"title": "Practice flashcards"},
        "3": {"title": "Exit"}}
menu_path = []
current_menu_level = menu
flashcards = {}


# region Methods
def show_menu(menu_dict):
    for menu_item in menu_dict.keys():
        if menu_item == "title":
            continue
        print(f"{menu_item}. {menu_dict[menu_item]['title']}")


def select_menu_item(menu_dict):
    selected_item_number = input()
    if selected_item_number in menu_dict.keys():
        return selected_item_number
    else:
        print(f"{selected_item_number} is not an option")
        return None


def execute_selected_item(menu_dict, item):
    global current_menu_level
    current_item = menu_dict[item]['title']
    if current_item == "Exit":
        if len(menu_path) > 0:
            current_menu_level = menu_path.pop()
        else:
            __exit__()
    elif current_item == "Add a new flashcard":
        add_flashcard()
    elif current_item == "Practice flashcards":
        start_practice()


def add_flashcard():
    question = ""
    answer = ""
    while question == "":
        question = input("Question:")
    while answer == "":
        answer = input("Answer:")
    flashcards.update({question: answer})


def start_practice():
    if len(flashcards.keys()) == 0:
        print("There is no flashcard to practice!")
        return

    for question, answer in flashcards.items():
        print(f"Question: {question}")
        is_show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower()
        while is_show_answer not in ['y', 'n']:
            print(f"{is_show_answer} is not an option")
            is_show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower()
        if is_show_answer == 'y':
            print(f"Answer: {answer}")


def __exit__():
    print("Bye!")
    exit()
# endregion


# region Main()
while True:
    show_menu(current_menu_level)
    selected_menu_item = select_menu_item(current_menu_level)
    if selected_menu_item is None:
        continue
    if len(current_menu_level[selected_menu_item]) > 1:
        menu_path.append(current_menu_level)
        current_menu_level = current_menu_level[selected_menu_item]
        continue
    execute_selected_item(current_menu_level, selected_menu_item)
# endregion
