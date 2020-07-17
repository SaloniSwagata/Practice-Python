# Uses python3
def calc_fib(n):
    a=0
    b=1
    f=0
    if n==1:
        return 0
    elif n==2:
        return 1
    for i in range(3,n+1):
        f=a+b
        a=b
        b=f
    return f

n = int(input())
print(calc_fib(n))
