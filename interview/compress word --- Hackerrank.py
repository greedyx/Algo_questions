'''
word = 'abbcccb', k =3  means can delete consecutive char
first : delete ccc, and then becomes 'abbb'
Second : delete bbb, and then becomes "a"
return a

word = 'abbcccbddddb', k =4
delete dddd
return "abbcccbb"
'''



def compressWord(word, k):
    # Write your code here
    stack = []
    for w in word:
        if not stack or w != stack[-1][0]:
            stack.append((w, 1))
        elif w == stack[-1][0]:
            count = stack[-1][1]
            if count + 1 < k:
                stack.append((w, count + 1))
            elif count + 1 == k:
                while stack and stack[-1][0] == w:
                    stack.pop()

    res = ""
    for pair in stack:
        res += pair[0]

    return res