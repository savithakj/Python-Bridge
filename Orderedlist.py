class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def add(self,item):
         current = self.head
         previous = None
         stop = False
         while current != None and not stop:
             if current.getData() > item:
                 stop = True
             else:
                 previous = current
                 current = current.getNext()

         temp = Node(item)
         if previous == None:
             temp.setNext(self.head)
             self.head = temp
         else:
             temp.setNext(current)
             previous.setNext(temp)
