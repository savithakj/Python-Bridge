class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def revstring(mystr):
    backwards = mystr[::-1]
    return(backwards)





testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')