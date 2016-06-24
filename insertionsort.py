def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index
     print(index,position,currentvalue,alist[position-1])
     while position>0 and alist[position-1]>currentvalue:
         print(position, currentvalue, alist[position - 1],alist)
         alist[position]=alist[position-1]
         position = position-1
         print(alist)
     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)