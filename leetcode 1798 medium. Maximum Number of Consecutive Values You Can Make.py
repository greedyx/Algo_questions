'''
示例 2：
输入：coins = [1,1,1,4]
输出：8
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
- 2：取 [1,1]
- 3：取 [1,1,1]
- 4：取 [4]
- 5：取 [4,1]
- 6：取 [4,1,1]
- 7：取 [4,1,1,1]
从 0 开始，你可以构造出 8 个连续整数。

示例 3：
输入：nums = [1,4,10,3,1]
输出：20

提示：
coins.length == n
1 <= n <= 4 * 10^4
1 <= coins[i] <= 4 * 10^4

'''

def getMaximumConsecutive(coins) -> int:
    coins.sort()
    v = 0  # we can make 0...v
    for i in range(len(coins)):
        if coins[i] <= v + 1:
            v += coins[i]
        else:
            break
    return v + 1  # [0...v]: v + 1 values
nums = [1,4,10,3,1]
print(getMaximumConsecutive(nums))