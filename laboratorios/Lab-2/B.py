from sys import stdin


def busq(lis,x,low,high):
    if int(low) > int(high):
        print("-1")
    else:
        mid = (int(low)+int(high))//2
        if x==int(lis[mid]):
            print(mid)
        elif x < int(lis[mid]):
            return busq(lis,x,low,mid-1)
        else:
            return busq(lis,x,mid+1,high)
        




def main():

    lis=[]
    x=int(stdin.readline().strip())
    a=stdin.readline().strip()
    for i in range(len(a)):
        if a[i]!="[" and a[i]!="]" and a[i]!=",":
            lis.append(a[i])
    busq(lis,x,0,len(lis)-1)


main()
