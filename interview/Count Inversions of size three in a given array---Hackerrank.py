'''
Input:  {9, 6, 4, 5, 8}
Output:  2
The two inversions are {9, 6, 4} and {9, 6, 5}
'''

'''
遍历考虑中间的数字，检查前面的是否大于mid,后面的是否小于mid
'''


# Returns count of inversions
# of size 3
def getInvCount(arr, n):
    # Initialize result
    invcount = 0

    for i in range(1, n - 1):

        # Count all smaller elements
        # on right of arr[i]
        small = 0
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                small += 1

        # Count all greater elements
        # on left of arr[i]
        great = 0;
        for j in range(i - 1, -1, -1):
            if (arr[i] < arr[j]):
                great += 1

        # Update inversion count by
        # adding all inversions that
        # have arr[i] as middle of
        # three elements
        invcount += great * small

    return invcount


# Driver program to test above function
arr = [8, 4, 2, 1]
n = len(arr)
print("Inversion Count :", getInvCount(arr, n))