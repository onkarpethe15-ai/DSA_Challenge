def pattern1(n):
    if n == 0:
        return
    print([n]*n)
    pattern1(n-1)


print(pattern1(5))
