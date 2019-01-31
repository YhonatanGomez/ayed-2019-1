from sys import stdin






def fib(n):
    if n<=1:
        return n,0
    else:
        a,b=fib(n-1)
    return a+b,a
    
def main():
    n=int(stdin.readline().strip())
    m=int(stdin.readline().strip())
    f=fib(n)
    f=f[0]
    print(f)
main()
