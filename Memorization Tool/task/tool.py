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
# endregion


# region Variables
menu = {"1": {"title": "Add flashcards", "is_executed": False,
              "1": {"title": "Add a new flashcard"},
              "2": {"title": "Exit"}
              },
        "2": {"title": "Practice flashcards", "is_executed": True,
              "y": {"title": 'press "y" to see the answer:'},
              "n": {"title": 'press "n" to skip:'},
              "u": {"title": 'press "u" to update:',
                    "d": {"title": 'press "d" to delete the flashcard:'},
                    "e": {"title": 'press "e" to edit the flashcard:'}
                    }
              },
        "3": {"title": "Exit"}}
menu_path = []
current_menu_level = menu
# endregion


# region Methods
def connect_to_sqlite_db(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()


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


def execute_selected_item(menu_dict, item, session_obj):
    global current_menu_level
    current_item = menu_dict[item]['title']
    if current_item == "Exit":
        if len(menu_path) > 0:
            current_menu_level = menu_path.pop()
        else:
            __exit__()
    elif current_item == "Add a new flashcard":
        add_flashcard(session_obj)
    elif current_item == "Practice flashcards":
        start_practice(session_obj)


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
    show_menu(current_menu_level)
    selected_menu_item = select_menu_item(current_menu_level)
    if selected_menu_item is None:
        continue
    if len(current_menu_level[selected_menu_item]) > 1:
        menu_path.append(current_menu_level)
        current_menu_level = current_menu_level[selected_menu_item]
        continue
    print()
    execute_selected_item(current_menu_level, selected_menu_item, session)
# endregion
