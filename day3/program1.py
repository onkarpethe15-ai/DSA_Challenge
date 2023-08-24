l = [4, 8, 2, 4, 7, 5]
final_list = [x for x in l if x % 2 == 0]
# print(final_list)
# list comhersension using if else
another_list = [x**3 if x % 2 == 0 else x**2 for x in l]
print(another_list)
