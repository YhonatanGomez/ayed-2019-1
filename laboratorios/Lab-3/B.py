from sys import stdin

def mergeSort(alist,cont):
    cont+=1
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,cont)
        mergeSort(righthalf,cont)

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
    print(cont)
    return alist



def main():
    lis=[]
    res=""
    n=int(stdin.readline().strip())
    a=stdin.readline().strip().split()
    for i in range(len(a)):
        lis.append(int(a[i]))
    c=mergeSort(lis,0)
    res=str(c[0])+" "+str(c[len(c)-1])
    print(res)


main()
