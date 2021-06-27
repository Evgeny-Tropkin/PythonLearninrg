# region Imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import MenuItem as toolMenu
# endregion

# region Classes
Base = declarative_base()


class FlashCard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    stage = Column(Integer)


# endregion

# region Variables
max_stage = 3
# endregion


# region Methods
def connect_to_sqlite_db(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    return session()


def create_menu():
    root = toolMenu.MenuItem(None, "root", "Main menu", False)
    # region Main menu
    # region item_1 (Add flashcard menu)
    item_1 = toolMenu.MenuItem(root, "1", "1. Add flashcards", False)
    item_1_1 = toolMenu.MenuItem(item_1, "1_1", "1. Add a new flashcard", True)
    item_1_2 = toolMenu.MenuItem(item_1, "1_2", "2. Exit", True)
    # endregion
    # region item_2 (Practice flashcards menu)
    item_2 = toolMenu.MenuItem(root, "2", "2. Practice flashcards", True)
    item_2_y = toolMenu.MenuItem(item_2, "2_y", 'press "y" to see the answer:', True)
    item_2_n = toolMenu.MenuItem(item_2, "2_n", 'press "n" to skip:', True)
    # region Item_2_yn (Check answer menu)
    item_2_yn_y = toolMenu.MenuItem(item_2_y, "2_yn_y", 'press "y" if your answer is correct:', True)
    item_2_yn_n = toolMenu.MenuItem(item_2_y, "2_yn_n", 'press "n" if your answer is wrong:', True)
    # end region
    item_2_u = toolMenu.MenuItem(item_2, "2_u", 'press "u" to update:', False)
    # region Item_2_u (Update flashcard menu)
    item_2_u_d = toolMenu.MenuItem(item_2_u, "2_u_d", 'press "d" to delete the flashcard:', True)
    item_2_u_e = toolMenu.MenuItem(item_2_u, "2_u_e", 'press "e" to edit the flashcard:', True)
    # endregion
    # end region
    # endregion
    # endregion
    # region item_3 (Exit)
    item_3 = toolMenu.MenuItem(root, "3", "3. Exit", True)
    # endregion

    # region Menu relations
    # region root (Main menu relations)
    root.set_nodes(item_1, item_2, item_3)
    # endregion)
    # region item_1 (Add flashcards menu relationships)
    item_1.set_nodes(item_1_1, item_1_2)
    # endregion
    # region item_2 (Practice flashcards menu relationships)
    item_2.set_nodes(item_2_y, item_2_n, item_2_u)
    item_2_y.set_nodes(item_2_yn_y, item_2_yn_n)
    item_2_n.set_nodes(item_2_yn_y, item_2_yn_n)
    # region item_2_u (Update flashcard menu relationships)
    item_2_u.set_nodes(item_2_u_d, item_2_u_e)
    # endregion
    # endregion
    # endregion

    return root


def show_menu(menu_item):
    menu_item_nodes = menu_item.get_nodes().values()
    for node in menu_item_nodes:
        print(node.get_title())


def select_menu_item(menu_item):
    while True:
        selected_item = input()
        if selected_item in menu_item.get_nodes().keys():
            nodes = menu_item.get_nodes()
            return nodes[selected_item]
        else:
            print(f"{selected_item} is not an option")
            return menu_item


def execute_selected_item(menu_item):
    menu_id = menu_item.get_id()

    if menu_id == "1_1":
        add_flashcard()
        return menu_item.get_parent()
    elif menu_id == "1_2":
        return menu_item.get_parent().get_parent()
    elif menu_id == "2":
        start_practice(menu_item)
        return menu_item.get_parent()
    elif menu_id == "3":
        __exit__()


def process_flashcard(menu_item, flashcard):
    menu_id = menu_item.get_id()

    if menu_id == "2_u":
        show_menu(menu_item)
        selected_item = select_menu_item(menu_item)
        menu_id = selected_item.get_id()

        if menu_id == "2_u_e":
            edit_flashcard(flashcard)
        elif menu_id == "2_u_d":
            current_session.delete(flashcard)
            current_session.commit()
        return

    elif menu_id == "2_y" or menu_id == "2_n":
        if is_answer_correct(menu_item, flashcard):
            change_stage_up(flashcard)
        else:
            reset_stage(flashcard)


def add_flashcard():
    entered_question = ""
    entered_answer = ""
    while entered_question == "":
        entered_question = input("Question:")
    while entered_answer == "":
        entered_answer = input("Answer:")
    current_session.add(FlashCard(question=entered_question, answer=entered_answer, stage=1))
    current_session.commit()


def edit_flashcard(flashcard):
    is_flashcard_data_changed = False

    print(f"current question: {flashcard.question}")
    print("please write a new question:")
    new_question = input()
    if new_question != "":
        flashcard.question = new_question
        is_flashcard_data_changed = True

    print()
    print(f"current answer: {flashcard.answer}")
    print("please write a new answer:")
    new_answer = input()
    if new_answer != "":
        flashcard.answer = new_answer
        is_flashcard_data_changed = True

    if is_flashcard_data_changed:
        current_session.commit()


def start_practice(menu_item):
    flashcards = current_session.query(FlashCard).all()

    if len(flashcards) == 0:
        print("There is no flashcard to practice!")
        return

    for flashcard in flashcards:
        print(f"Question: {flashcard.question}")
        show_menu(menu_item)
        selected_menu_item = select_menu_item(menu_item)
        process_flashcard(selected_menu_item, flashcard)

        print()


def is_answer_correct(menu_item, flashcard):
    menu_id = menu_item.get_id()

    if menu_id == "2_y":
        print(f"Answer: {flashcard.answer}")

    show_menu(menu_item)
    selected_item = select_menu_item(menu_item)

    return selected_item.get_id() == "2_yn_y"


def change_stage_up(flashcard):
    flashcard.stage += 1
    if flashcard.stage > max_stage:
        current_session.delete(flashcard)
    current_session.commit()


def reset_stage(flashcard):
    flashcard.stage = 1
    current_session.commit()


def __exit__():
    print("Bye!")
    current_session.close()
    exit()


# endregion

# region Main()
def main():
    current_menu_level = create_menu()

    while True:
        show_menu(current_menu_level)
        selected_item = select_menu_item(current_menu_level)
        if selected_item.is_executed():
            current_menu_level = execute_selected_item(selected_item)
        else:
            current_menu_level = selected_item


# region Script
if __name__ == "__main__":
    current_session = connect_to_sqlite_db("sqlite:///flashcard.db?check_same_thread=False")
    main()
# endregion
# endregion
