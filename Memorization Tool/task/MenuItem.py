class MenuItem:
    def __init__(self, menu_id, parent, title):
        self.menu_id = menu_id
        self.parent = parent
        self.title = title
        self.nodes = {}
