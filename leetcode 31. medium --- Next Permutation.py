'''
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        首先说一下这题怎么想到的。有如下的一个数组

        1　　2　　7　　4　　3　　1

        下一个排列为：

        1　　3　　1　　2　　4　　7

        7431倒序，然后把第一个比2大的数字换位置，此处为3
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break

    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        for k in range(i, (i + j) // 2 + 1):
            self.swap(nums, k, i + j - k)

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]

test = Solution()
nums = [1,2,7,4,3,1]
test.nextPermutation(nums)
print(nums)
# [1, 3, 1, 2, 4, 7]