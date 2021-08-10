x = {1: (2,3), 3: (4,5), 4: (3,1), 2: (1,-1), 0: (0,100)}

b = sorted(x.items(), key=lambda item: item[1][1])
print(b)
# [(2, (1, -1)), (4, (3, 1)), (1, (2, 3)), (3, (4, 5)), (0, (0, 100))]

c = sorted(x.items(), key=lambda item: item[1][0])
print(c)
# [(0, (0, 100)), (2, (1, -1)), (1, (2, 3)), (4, (3, 1)), (3, (4, 5))]

d = sorted(x.items(), key=lambda item: item[0])
print(d)
# [(0, (0, 100)), (1, (2, 3)), (2, (1, -1)), (3, (4, 5)), (4, (3, 1))]

c = sorted(x.items(), key=lambda item: item[1][0],reverse=True)
print(c)
# [(3, (4, 5)), (4, (3, 1)), (1, (2, 3)), (2, (1, -1)), (0, (0, 100))]