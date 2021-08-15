'''
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are
"abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
'''


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = j = 0
        d = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        while j < n:
            d[s[j]] += 1
            j += 1
            while min(d.values()) > 0:  # once three characters all show up
                # the string which ends behind the right pointer will count
                res += n - j + 1
                d[s[i]] -= 1
                i += 1

        return res


s = Solution()

print(s.numberOfSubstrings("abcabc"))
