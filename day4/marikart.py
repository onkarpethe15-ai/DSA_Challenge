# Input:
#     5 2
#     3 37
#     1 41
#     2 37
#     5 41
#     4 35
# Output:
#     2 3
# Explanation:
#      5 2 is the size of the leaderboard. The second lowest score is 37 and their corresponding players are 2 and 3.


# soln =>
mat = [[3, 37], [1, 41], [2, 37], [5, 41], [4, 35]]
l = []
for i in range(len(mat)):
    l.append(mat[i][1])
print(l)
x = list(set(l))
x.sort()
print(x)
temp = x[1]
sol = []
print(temp)
for i in range(len(mat)):
    if temp == mat[i][1]:
        sol.append(mat[i][0])
print(sol)
