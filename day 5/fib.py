def fib(n):
    if n == 0 or n == 1:
        return n
    f1 = fib(n-1)
    f2 = fib(n-2)
    ans = f1 + f2
    return ans


print(fib(4))
