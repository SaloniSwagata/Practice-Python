

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    digit = 0

    for _ in range(2,n+1):
        digit = (previous+current)%10
        previous=current
        current = digit
    return digit

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
