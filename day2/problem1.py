# Given an array arr of size n, and two intervals x and y. Find the average of elements which lies between the given intervals inclusively.
# sol :
def solve(n, arr, x, y):
    # CODE HERE
    avg = 0
    counter = 0
    for i in range(x, y+1):
        counter = counter + 1
        avg = avg + arr[i]
    return avg/counter
