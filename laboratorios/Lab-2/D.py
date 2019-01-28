from sys import stdin



def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return alist

 
def recur(lis,cont,v):
    for i in range(len(lis)):
        if i+1<len(lis):
            if lis[i]==lis[i+1]:
                cont=cont+1
            elif lis[i]!=lis[i+1]:
                cont=1
            if cont>v:
                print(True)
                break
            else:
                print(False)
def main():
    n=int(stdin.readline().strip())
    a=stdin.readline().strip()
    lis=[]
    for i in range(len(a)):
        if a[i]!="[" and a[i]!="]" and a[i]!=",":
            lis.append(int(a[i]))
    v=n//2
    lis=mergeSort(lis)
    recur(lis,1,n//2)
            



main()
