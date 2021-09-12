'''
space = [2,5,4,6,8]
x = 3

moving window with 3 numbers minimum is [2,4,4]
Then take maximum , return 4
'''


space = [2,5,4,6,8]
x = 3


def segment(x,space):
    import collections

    output = []
    q = collections.deque()
    l = r = 0

    # Put index in q
    while r < len(space):
        while q and space[q[-1]] > space[r]:
            q.pop()
        q.append(r)

        # we shall keep q[0] is the leftmost index in q
        # remove left val from window if left index already bigger than q[0]
        if l > q[0]:
            q.popleft()

        if (r + 1) >= x:
            output.append(space[q[0]])
            l += 1
        r += 1

    return max(output)

print(segment(x,space))