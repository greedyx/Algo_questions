'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

# https://www.youtube.com/watch?v=8f1XPm4WOUc
# union find
# Can refer to 547, similar question

class Solution:
    def findCircleNum(self, isConnected) -> int:

        rela = {}

        # 找父节点
        def find(k):
            rela.setdefault(k, k)
            if rela[k] != k:
                rela[k] = find(rela[k])
            return rela[k]

        # 合并父节点
        def union(a, b):
            rela[find(b)] = find(a)

        n = len(isConnected)
        count = n
        # above code is model

        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    union(i, j)
                    count -= 1
        return count

test = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
a  = test.findCircleNum(isConnected)
print(a)