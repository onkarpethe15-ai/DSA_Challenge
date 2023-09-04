# Given an sorted array arr of size n and an integer key. If the target exists in the array, return its index. If not, return the index where it would be if it were inserted in order.

# Input Format
# First Parameter - number n

# Second Parameter - array arr of size n

# Third Parameter - number key

# Output Format
# Return the number.

# Example 1:
# Input:
#     5
#     1 3 4 5 10
#     2
# Output:
#     1
# Explanation:
#     Since 2 is missing from the given array, it would be inserted at index 1.
# Example 2:
# Input:
#     5
#     1 3 8 9 11
#     9
# Output:
#     3
# Explanation:
#     The key 9 was found at index 3.
# Constraints
# 1 < n <= 104
# -104 <= arr[i], key <= 104
# All the integers in arr are unique.
# arr is sorted in ascending order.
# Expected Time Complexity: O(log n)
# Expected Space Complexity: O(1)
def solve(n, arr, key):
    left_ptr = 0
    right_ptr = len(arr)-1
    if (len(arr) == 1):
        if arr[0] < key:
            return 1
        else:
            return 0
    if len(arr) == 0:
        return 0
    while (left_ptr <= right_ptr):
        mid_elem = (left_ptr+right_ptr) // 2
        if arr[mid_elem] == key:
            return mid_elem
        elif (arr[mid_elem] > key):
            right_ptr = mid_elem-1
        else:
            left_ptr = mid_elem+1
    return left_ptr
