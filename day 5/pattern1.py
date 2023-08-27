def pattern1(n):
    if n == 0:
        return
    pattern1(n-1)
    print([n]*n)


print(pattern1(5))
