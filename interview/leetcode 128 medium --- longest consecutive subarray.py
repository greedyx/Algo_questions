'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


def longestConsecutive(nums) -> int:
    nums = set(nums)
    maxi = 0
    for number in nums:
        if number - 1 not in nums:
            temp = 1
            while number + 1 in nums:
                temp += 1
                number += 1
            maxi = max(maxi, temp)
    return maxi
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))