def fact(n):
    if n == 1:
        return 1
    f = fact(n-1)
    ans = n*f
    return ans


print(fact(5))
