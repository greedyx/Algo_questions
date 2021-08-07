'''
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.
requirement : O(n) time complexity
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
'''


import random


class Solution2(object):
    def wiggleSort(self, nums):
        """
        First use Quickselect to find the median, O(n)
        And then for loop we can construct a list meets the requirement
        Seems there is a way to do it with O(1) space complexity but here is good enough for me, I think
        """
        median = self.quick_select(nums,len(nums)//2)
        res = [0] * len(nums)
        even = 0
        odd = 1
        for number in nums:
            if number <= median:
                res[even] = number
                even += 2
            else:
                res[odd] = number
                odd += 2
        return res


    def quick_select(self,A, k):
        # pivot value is random
        pivot = random.choice(A)

        A1 = []  # values < pivot
        A2 = []  # values > pivot

        for i in A:
            if i < pivot:
                A1.append(i)
            elif i > pivot:
                A2.append(i)
            else:
                pass  # ignore Pivot value!

        # case 1: median is in A1
        if k <= len(A1):
            return self.quick_select(A1, k)
        # case 2: median is in A2
        elif k > len(A) - len(A2):
            return self.quick_select(A2, k - (len(A) - len(A2)))
        # case 3: median found
        else:
            return pivot

nums =  [1,5,1,1,6,4]
test = Solution2()
print(test.wiggleSort(nums))