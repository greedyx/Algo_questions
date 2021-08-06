class Solution:
    def subarraySum(self, nums, k) -> int:
        # 这方法的基于一个idea：sum[j] - sum[i] == k的话，nums[i , j ]之间数字的和就是k。比如sum[j]跟sum[i]是一样的，那中间这段加起来就是0。
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)  # sums 表示现在指向哪个值，减去k后到的是起点的位置，起点值有几个，则count + 几
            d[sums] = d.get(sums, 0) + 1

        return (count)

nums = [1,2,3]
k = 3
test = Solution()
print(test.subarraySum(nums,k))