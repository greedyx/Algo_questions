# 1 construct dict
dict3 = dict(zip(["one", "two", "three"], [1, 2, 3]))
dict4 = dict([("one", 1), ("two", 2), ("three", 3)])


# 2 sort dict by values
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

from operator import itemgetter

stu = [
	{"id": 3, "name": "Tom", "score": 82},
	{"id": 2, "name": "Jerry", "score": 67},
	{"id": 1, "name": "Pig", "score": 82},
	{"id": 4, "name": "Dog", "score": 98},
]
# 根据key"score"对应的value 对stu正序排序
'''
[{'id': 2, 'name': 'Jerry', 'score': 67},
{'id': 3, 'name': 'Tom', 'score': 82},
{'id': 1, 'name': 'Pig', 'score': 82},
{'id': 4, 'name': 'Dog', 'score': 98}]
'''
sorted_by_score = sorted(stu, key=itemgetter("score"))
print(sorted_by_score)

# 根据key"score"对应的value 对stu逆序排序
'''
[{'id': 4, 'name': 'Dog', 'score': 98},
{'id': 3, 'name': 'Tom', 'score': 82},
{'id': 1, 'name': 'Pig', 'score': 82},
{'id': 2, 'name': 'Jerry', 'score': 67}]
'''
sorted_by_score_rev = sorted(stu, key=itemgetter("score"), reverse=True)
print(sorted_by_score_rev)

# 根据key"score"和"id" 对stu正序排序(先根据"score"排序，"score"相同的情况下根据"id"排序)
'''
[{'id': 2, 'name': 'Jerry', 'score': 67},
{'id': 1, 'name': 'Pig', 'score': 82},
{'id': 3, 'name': 'Tom', 'score': 82},
{'id': 4, 'name': 'Dog', 'score': 98}]
'''
rows_by_score_id = sorted(stu, key=itemgetter("score", "id"))
print(rows_by_score_id)










# 3 del item from dict
x = {1: (2,3), 3: (4,5), 4: (3,1), 2: (1,-1), 0: (0,100)}
x.pop(0) # key = 0
x.popitem() # remove the last element of dict
del x[1]
print(x)
# {3: (4, 5), 4: (3, 1)}



# 4 dict update
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
print(d1)
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}

d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
print(d1)
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}



# 5 dict max/min
dict1 = {"a": 123, "b": 321, "c": 200}

# 获取max value及其对应的key
max_tuple = max(zip(dict1.values(), dict1.keys()))
print(max_tuple)  # (321, 'b')

# 获取min value及其对应的key
min_tuple = min(zip(dict1.values(), dict1.keys()))
print(min_tuple)  # (123, 'a')

dict1 = {"a": 123, "b": 321, "c": 200}


# 在一个字典上执行普通的数学运算，它们仅仅作用于键，而不是值
max_key = max(dict1)
print(max_key)  # 返回key的最大值 'c'

# 获取最大值对应的键
max_value_key = max(dict1, key=lambda k: dict1[k])
print(max_value_key)  # 'b'
# 根据键获取对应的值
max_value = dict1[max_key]
print(max_value)  # 321


# 并集 |  以第一个dict为准
a = {"one": 1, "two": 2, "three": 3}
b = {"one": 111, "three": 3, "four": 4}

c = dict(a.items() | b.items())
print(c)  # key"one"的值没有被修改 {'four': 4, 'one': 1, 'three': 3, 'two': 2}



# 交集 &
a = {"one": 1, "two": 2, "three": 3}
b = {"one": 111, "three": 3, "four": 4}

c = dict(a.items() & b.items())
print(c)  # {'three': 3}


# 差集  从第一个字典中移除与第二个字典相同的键值对
a = {"one": 1, "two": 2, "three": 3}
b = {"one": 111, "three": 3, "four": 4}

c = dict(a.items() - b.items())
print(c)  # {'two': 2, 'one': 1}
