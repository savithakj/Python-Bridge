class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palcheck(s):
   word=Deque()
   for ch in s:
       word.addRear(ch);
   #print(word.items)
   flag=0
   while (word.isEmpty())==True:
    if word.removeFront()==word.removeRear():
          continue
    else:
           flag=1
           break
   if flag==1:
     return ("Not Palindrome")
   else:
     return ("Palindrome")


print(palcheck("Malayalam"))
