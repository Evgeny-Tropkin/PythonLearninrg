class Stack():

    def __init__(self):
        self.store = []

    def push(self, el):
        self.store.append(el)

    def pop(self):
        return self.store.pop()

    def peek(self):
        return self.store[-1]

    def is_empty(self):
        return len(self.store) == 0
