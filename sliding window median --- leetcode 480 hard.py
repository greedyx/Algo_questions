
'''
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
'''


import bisect

class Solution:
  def medianSlidingWindow(self, nums, k):
    if k == 0: return []
    ans = []
    window = sorted(nums[0:k])
    for i in range(k, len(nums) + 1):
      ans.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)
      if i == len(nums):
          break
      index = bisect.bisect_left(window, nums[i - k])
      window.pop(index)
      bisect.insort_left(window, nums[i])
    return ans


# Bisect is something about binary search or insert

'''
def binary_search(t,x):
    temp = t;
    temp.sort();
    low = 0;
    mid = 0;
    high = len(temp)-1;
    while low < high:
        mid = (low+high)/2;
        if x<t[mid]:
            high = mid-1;
        elif x>t[mid]:
            low = mid+1;
        else:
            return mid-1; #是否等价与bisect_left;
'''