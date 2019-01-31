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




def imprimir(c,cont,lis,cont2):
    if cont2==len(c):
        print(lis)
    elif cont2==10:
        print(lis)
    else:
        lis.append(c[cont])
        return imprimir(c,cont-1,lis,cont2+1)
    
    










def main():
    a=[]
    s=stdin.readline().strip().split()
    for i in range(len(s)):
        a.append(int(s[i]))
    c=mergeSort(a)
    
    imprimir(c,len(c)-1,[],0)

main()
