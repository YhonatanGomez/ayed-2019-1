from sys import stdin




def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return alist

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def main():
    lis=[]
    n=int(stdin.readline().strip())
    a=stdin.readline().strip().split(",")
    b=list(a[0])
    c=list(a[len(a)-1])
    b[0] = ""
    c[len(c)-1]=""
    b="".join(b)
    c="".join(c)
    a[0]=b
    a[len(a)-1]=c
    for i in range(len(a)):
       lis.append(int(a[i]))
    q=quickSort(lis)
    print(q)
main()
