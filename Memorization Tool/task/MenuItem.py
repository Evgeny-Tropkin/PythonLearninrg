class MenuItem:
    def __init__(self, menu_id, parent, title):
        self.__menu_id = menu_id
        self.__parent = parent
        self.__title = title
        self.__nodes = {}
