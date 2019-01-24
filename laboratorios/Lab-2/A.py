from sys import stdin


def mul(lis,cont,may,x):
    if cont==len(lis):
        lis[x]=0
        return may
    else:
        if cont==0:
            may=int(lis[cont])
        else:
            if may<int(lis[cont]):
                may=int(lis[cont])
                x=cont
        return mul(lis,cont+1,may,x)
        
    





def main():
    lis=stdin.readline().strip().split()
    cont=0
    lista=[]
    while cont<2:
        a=mul(lis,0,0,0)
        cont=cont+1
        lista.append(a)
    print(lista[0]*lista[1])
        
    


main()
