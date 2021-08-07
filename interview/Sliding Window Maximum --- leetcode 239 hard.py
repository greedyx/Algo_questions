'''
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''



import collections

def maxSlidingWindow(nums,k):
    output = []
    q = collections.deque()
    l = r = 0

    # Put index in q
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # we shall keep q[0] is the leftmost index in q
        # remove left val from window if left index already bigger than q[0]
        if l > q[0]:
            q.popleft()

        if (r+1)>= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))