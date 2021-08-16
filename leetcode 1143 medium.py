'''
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
'''



# dp，matrix[][]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        t = [[0 for p in range(0, m + 1)]
             for q in range(0, n + 1)]

        for a in range(0, n + 1):
            t[a][0] = 0

        for b in range(1, m + 1):
            t[0][b] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if text1[i - 1] == text2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]

                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        return t[n][m]