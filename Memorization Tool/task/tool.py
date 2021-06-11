from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# region Classes
Base = declarative_base()


class FlashCard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


class MenuItem:
    def __init__(self, parent, title):
        self.parent = parent
        self.title = title
        self.nodes = {}
        self.for_exit = None
# endregion


# region Variables
root = MenuItem(None, "Main menu")
# region Main menu
# region item_1 (Add flashcard menu)
item_1 = MenuItem(root, "Add flashcards")
item_1_1 = MenuItem(item_1, "Add a new flashcard")
item_1_2 = MenuItem(item_1, "Exit")
# endregion
# region item_2 (Practice flashcards menu)
item_2 = MenuItem(root, "Practice flashcards")
item_2_y = MenuItem(item_2, 'press "y" to see the answer:')
item_2_n = MenuItem(item_2, 'press "n" to skip:')
item_2_u = MenuItem(item_2, 'press "u" to update:')
# region Item_2_u (Update flashcard menu)
item_2_u_d = MenuItem(item_2_u, 'press "d" to delete the flashcard:')
item_2_u_e = MenuItem(item_2_u, 'press "e" to edit the flashcard:')
# end region
# endregion
# endregion
# region Menu relations
# region root (Main menu relations)
root.nodes = {1: item_1, 2: item_2}
# endregion)
# region item_1 (Add flashcards menu relationships)
item_1.nodes = {1: item_1_1, 2: item_1_2}
# endregion
# region item_2 (Practice flashcards menu relationships)
item_2.nodes = {'y': item_2_y, 'n': item_2_n, 'u': item_2_u}
# region item_2_u (Update flashcard menu relationships)
item_2_u.nodes = {'e': item_2_u_e, 'd': item_2_u_d}
# endregion
# endregion
# endregion
# endregion

current_menu_level = root
# endregion


# region Methods
def connect_to_sqlite_db(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()


def show_menu():
    pass


def select_menu_item():
    pass


def execute_selected_item():
    pass


def add_flashcard(session_obj):
    entered_question = ""
    entered_answer = ""
    while entered_question == "":
        entered_question = input("Question:")
    while entered_answer == "":
        entered_answer = input("Answer:")
    session_obj.add(FlashCard(question=entered_question, answer=entered_answer))
    session_obj.commit()


def start_practice(session_obj):
    flashcards = session_obj.query(FlashCard).all()

    if len(flashcards) == 0:
        print("There is no flashcard to practice!")
        return

    for item in flashcards:
        print(f"Question: {item.question}")
        is_show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower()
        while is_show_answer not in ['y', 'n']:
            print(f"{is_show_answer} is not an option")
            is_show_answer = input('Please press "y" to see the answer or press "n" to skip:').lower()
        if is_show_answer == 'y':
            print(f"Answer: {item.answer}")
        print()


def __exit__():
    print("Bye!")
    exit()
# endregion


# region Main()
session = connect_to_sqlite_db("sqlite:///flashcard.db?check_same_thread=False")
while True:
    show_menu()

# endregion
