import random


def quick_select(A, k):
    # pivot value is random
    pivot = random.choice(A)

    A1 = []  # values < pivot
    A2 = []  # values > pivot

    for i in A:
        if i < pivot:
            A1.append(i)
        elif i > pivot:
            A2.append(i)
        else:
            pass  # ignore Pivot value!

    # case 1: median is in A1
    if k <= len(A1):
        return quick_select(A1, k)
    # case 2: median is in A2
    elif k > len(A) - len(A2):
        return quick_select(A2, k - (len(A) - len(A2)))
    # case 3: median found
    else:
        return pivot

A = [7,6,5,4,3,2,1]
i = 3
print(quick_select(A,i))