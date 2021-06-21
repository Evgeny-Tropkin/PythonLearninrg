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


# endregion

# region Variables

# endregion


# region Methods
def connect_to_sqlite_db(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    return session()


def create_menu():
    root = toolMenu.MenuItem(None, "root", "Main menu")
    # region Main menu
    # region item_1 (Add flashcard menu)
    item_1 = toolMenu.MenuItem(root, "1", "1. Add flashcards")
    item_1_1 = toolMenu.MenuItem(item_1, "1_1", "1. Add a new flashcard")
    item_1_2 = toolMenu.MenuItem(item_1, "1_2", "2. Exit")
    # endregion
    # region item_2 (Practice flashcards menu)
    item_2 = toolMenu.MenuItem(root, "2", "2. Practice flashcards")
    item_2_y = toolMenu.MenuItem(item_2, "2_y", 'press "y" to see the answer:')
    item_2_n = toolMenu.MenuItem(item_2, "2_n", 'press "n" to skip:')
    item_2_u = toolMenu.MenuItem(item_2, "2_u", 'press "u" to update:')
    # region Item_2_u (Update flashcard menu)
    item_2_u_d = toolMenu.MenuItem(item_2_u, "2_u_d", 'press "d" to delete the flashcard:')
    item_2_u_e = toolMenu.MenuItem(item_2_u, "2_u_e", 'press "e" to edit the flashcard:')
    # end region
    # endregion
    # endregion
    # region item_3 (Exit)
    item_3 = toolMenu.MenuItem(root, "3", "3. Exit")
    # endregion

    # region Menu relations
    # region root (Main menu relations)
    root.set_nodes(item_1, item_2, item_3)
    # endregion)
    # region item_1 (Add flashcards menu relationships)
    item_1.set_nodes(item_1_1, item_1_2)
    # endregion
    # region item_2 (Practice flashcards menu relationships)
    item_2.set_nodes(item_2_n, item_2_y, item_2_u)
    # region item_2_u (Update flashcard menu relationships)
    item_2_u.set_nodes(item_2_u_d, item_2_u_e)
    # endregion
    # endregion
    # endregion

    return root


def show_menu(menu_item):
    for title in menu_item.get_nodes().values():
        print(title)


def select_menu_item(menu_item):
    while True:
        selected_item = input()
        if selected_item in menu_item.get_nodes().keys():
            nodes = menu_item.get_nodes()
            return nodes[selected_item]
        else:
            print(f"{selected_item} is not an option")


def execute_selected_item(menu_item):
    menu_id = menu_item.get_id

    if menu_id == "1_1":
        add_flashcard(current_session)
        return menu_item.get_parent()
    elif menu_id == "1_2":
        return menu_item.get_parent().get_parent()
    elif menu_id == "2":
        start_practice(current_session, menu_item)


def process_flashcard(menu_item, flashcard):
    menu_id = menu_item.get_id

    if menu_id == "2_y":
        print(f"Answer: {flashcard.answer}")
    if menu_id == "2_u":
        update_flashcard(menu_item, flashcard)


def update_flashcard(menu_item, flashcard):
    show_menu(menu_item)
    selected_item = select_menu_item(menu_item)


def add_flashcard(session_obj):
    entered_question = ""
    entered_answer = ""
    while entered_question == "":
        entered_question = input("Question:")
    while entered_answer == "":
        entered_answer = input("Answer:")
    session_obj.add(FlashCard(question=entered_question, answer=entered_answer))
    session_obj.commit()


def start_practice(session_obj, menu_item):
    flashcards = session_obj.query(FlashCard).all()

    if len(flashcards) == 0:
        print("There is no flashcard to practice!")
        return

    for flashcard in flashcards:
        print(f"Question: {flashcard.question}")
        selected_menu_item = select_menu_item(menu_item)
        process_flashcard(selected_menu_item, flashcard)
        # is_show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower()
        # while is_show_answer not in ['y', 'n']:
        #     print(f"{is_show_answer} is not an option")
        #     is_show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower()
        # if is_show_answer == 'y':
        #     print(f"Answer: {item.answer}")
        print()


def __exit__():
    print("Bye!")
    exit()


# endregion

# region Main()
def main():
    current_menu_level = create_menu()

    while True:
        show_menu(current_menu_level)
        selected_item = select_menu_item(current_menu_level)
        if len(selected_item.get_nodes) == 0:
            current_menu_level = execute_selected_item(selected_item)
        else:
            current_menu_level = selected_item


# region Script
if __name__ == "__main__":
    current_session = connect_to_sqlite_db("sqlite:///flashcard.db?check_same_thread=False")
    main()
# endregion
# endregion
