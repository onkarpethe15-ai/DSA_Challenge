# Given an array of integers nums which are sorted in ascending order, and an integer target, write a function to search target in nums. If the target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Input Format
# First Parameter - number n

# Second Parameter - array of integers nums of size n

# Third Parameter - number target

# Output Format
# Return the number

# Example 1
# Input:
#     6
#     -1 0 3 5 9 12
#     9
# Output:
#     4
# Explanation:
#     Explanation: 9 exists in nums and its index is 4
# Example 2
# Input:
#     6
#     -1 0 3 5 9 12
#     2
# Output:
#     -1
# Explanation:
#     2 does not exist in nums so return -1
# Constraints
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique, nums is sorted in ascending order.
# Expected Time Complexity: O(log n)
# Expected Space Complexity: O(1)

def solve(n, nums, target):
    # CODE HERE
    left_ptr = 0
    right_ptr = len(nums)-1
    while (left_ptr <= right_ptr):
        mid_elem = (left_ptr+right_ptr) // 2
        if nums[mid_elem] == target:
            return mid_elem
        elif nums[mid_elem] > target:
            right_ptr = mid_elem-1
        else:
            left_ptr = mid_elem+1
    return -1
