# Given an integer array 'nums’, return 1(true) if any value appears at least twice in the array, and return 0(false) if every element is distinct.

# Input Format
# First Parameter - Number n

# Second Parameter - Array of Integer arr

# Output Format
# Return the integer(0 or 1)

# Example 1:
# Input:
#     4
#     1 2 3 1
# Output:
#     1
# Explanation:
#     '1' is repeated two times.
# Example 2:
# Input:
#     4
#     1 2 3 4 
# Output:
#     0
# Explanation:
#     No values are repeated.


# =>

def solve(n, arr):
    # CODE HERE
    list1 = arr
    for i in  arr:
        if arr.count(i) > 1:
            return 1
    return 0        
