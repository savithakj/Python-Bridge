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

def convert(num):
    s=Stack()
    while num!=0:
        rem=num%2
        #print(rem)
        s.push(rem)
        num=int(num/2)
       # print(num)
    binary=""
    while s.isEmpty()== False:
        dig=s.pop()
       # bin=(bin*10)+dig
        binary= binary +str(dig)
    return binary


print (convert(233))

