'''
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
'''

# https://www.youtube.com/watch?v=8f1XPm4WOUc
# Union Find

def countComponents(n,edges):
    # 每个节点是他们自己的父节点，初始
    par = [i for i in range(n)]
    # 每个节点含有多少个子节点，初始
    rank = [1] * n

    # 找父节点
    def find(n1):
        res = n1
        while res != par[res]:
            par[res] = par[par[res]]
            res = par[res]
        return res

    def union(n1,n2):
        p1,p2 = find(n1),find(n2)

        # 如果父节点相同说明已经合并了，不用再管
        if p1 == p2:
            return 0

        # 将父节点更新为比较大的集合的父节点
        # 然后将两个集合包含的子节点个数合并
        if rank[p2] > rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n
    for n1,n2 in edges:
        res -= union(n1,n2)
    return res

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(countComponents(n,edges))