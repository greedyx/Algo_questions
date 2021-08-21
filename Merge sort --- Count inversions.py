'''
[1, 20, 6, 4, 5]
(20,6) ,(20,4),(6,4) and so on, in total 5 inverse number pairs


use merge sort   O(n*logn)
no calculations during "divide" process
during "merge" process, observe how many numbers behind the medium value and calculate
使用分治算法，递归将数组进行二分（low ~ middle 和 middle+1 ~ high），直至为仅剩1个元素。此时逆序对数量为0。
再将数组（low ~ middle 和 middle+1 ~ high）两两依次合并，合并时若左半部分数组中的元素，则逆序对数量增加

'''


def inversion(A):
    lent = len(A)
    if lent < 2:
        return 0, A
    mid = lent // 2
    left = A[:mid]
    right = A[mid:]
    count_left, left = inversion(left)
    count_right, right = inversion(right)
    count_left_right, mergeA = merge(left, right)
    return count_left + count_right + count_left_right, mergeA


def merge(left, right):
    alist = []
    lenl = len(left)
    lenr = len(right)
    i, j, inver = 0, 0, 0
    while i < lenl and j < lenr:
        if left[i] <= right[j]:  # left[i]于right[j]及right[i]的元素都不构成逆序对
            alist.append(left[i])
            i += 1
        else:
            inver += lenl - i  # 先计数，再排序
            alist.append(right[j])
            j += 1
    while i < lenl:
        alist.append(left[i])
        i += 1
    while j < lenr:
        alist.append(right[j])
        j += 1
    return inver, alist


if __name__ == "__main__":
    list = [1, 20, 6, 4, 5]
    print(list)
    print(inversion(list))
