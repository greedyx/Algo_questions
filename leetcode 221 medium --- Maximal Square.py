'''
Given an m x n binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
'''


# From bottom to top

class Solution:
    def maximalSquare(self, matrix) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2


class Solution2:
    def maximalSquare(self, matrix) -> int:
        ans=0
        area=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            area[i][0]=int(matrix[i][0])
            ans=max(ans,area[i][0])
        for j in range(len(matrix[0])):
            area[0][j]=int(matrix[0][j])
            ans=max(ans,area[0][j])
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=="0":
                    area[i][j]=0
                else:
                    area[i][j]=min(area[i-1][j],area[i][j-1],area[i-1][j-1])+1
                ans=max(ans,area[i][j])
        return ans**2

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
test = Solution()
test2 = Solution2()
print(test.maximalSquare(matrix))
print(test2.maximalSquare(matrix))