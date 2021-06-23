class MenuItem:
    def __init__(self, parent, menu_id, title):
        self.__menu_id = menu_id
        self.__parent = parent
        self.__title = title
        self.__nodes = {}

    def get_id(self):
        return self.__menu_id

    def get_parent(self):
        return self.__parent

    def get_title(self):
        return self.__title

    def get_nodes(self):
        return self.__nodes

    def set_nodes(self, *nodes):
        for node in nodes:
            node_id = node.get_id()
            key = node_id[-1]
            self.__nodes.update({key: node})
