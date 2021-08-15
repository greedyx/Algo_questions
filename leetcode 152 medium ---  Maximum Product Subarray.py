'''
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''


class Solution:
    def maxProduct(self, nums) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)
        return res

test = Solution()
nums = [2,3,-2,4]
print(test.maxProduct(nums))