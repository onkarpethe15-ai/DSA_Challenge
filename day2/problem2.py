# Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.
# sol :
def solve(str1):
    # CODE HERE
    dic = {}
    sol = []
    for char in str1:
        if (char not in dic):
            dic[char] = 1
        else:
            dic[char] += 1
    for k, v in dic.items():
        sol.append(v)
    return sol
