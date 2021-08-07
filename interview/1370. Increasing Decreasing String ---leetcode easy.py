'''

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
'''

class Solution:
    def sortString(self, s: str) -> str:
        dicto={}
        res=''
        for i in list(map(chr,range(97,123))):
            dicto[i]=s.count(i)
        while set(dicto.values())!=set([0]):
            for i in dicto.keys():
                if dicto[i]>0:
                    res=res+i
                    dicto[i]-=1
            for i in reversed(dicto.keys()):
                if dicto[i]>0:
                    res=res+i
                    dicto[i]-=1
        return res

test = Solution()
s = "aaaabbbbcccc"
print(test.sortString(s))