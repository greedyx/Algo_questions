'''
https://www.youtube.com/watch?v=-RDzMJ33nx8
Distinct Subsequences - Dynamic Programming - Leetcode 115 - Python

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
'''

class Solution:

    def numDistinct(self,s,t):
        cache = {}

        def dfs(i,j):
            # t already empty
            if j == len(t):
                return 1
            # s already empty
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]

            # we will continue check whether i+1 equals to j, and use both results
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[(i,j)] = dfs(i+1,j)
            return cache[(i,j)]

        return dfs(0,0)

s = "rabbbit"
t = "rabbit"
test = Solution()
print(test.numDistinct(s,t))
