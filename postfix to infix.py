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
def postfixtoinfix(post):
    s=Stack()
    tokenlist=post.split()
    infix=[]
    for token in tokenlist:
        print(token)
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ " or token in "0123456789":
            s.push(int(token))
            print("Push")
        else:
            #while(s.isEmpty()==False):
                operand2 = s.pop()
                operand1 = s.pop()
                print("pop")
                print(operand1,operand2)
                result = doMath(token, operand1, operand2)
                print("Push",result)
                s.push(result)
    return s.pop()

def doMath(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

print(postfixtoinfix('17 10 + 3 * 9 / == '))
