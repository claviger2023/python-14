n = 10

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = fibonacci (n-2) + fibonacci (n-1)
        print(f)
    return f

fibonacci(n)