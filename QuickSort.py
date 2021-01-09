# Implementing Quick Sort using Python
# Date: 01/04/2021
# Author: Pranav H. Deo

import numpy as np


def Partition(arr, l, h):
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i + 1


def QuickSort(L, low, high):
    if low < high:
        pi = Partition(L, low, high)
        QuickSort(L, low, pi-1)
        QuickSort(L, pi+1, high)
    return L


MyList = np.random.randint(0, 500, 100)
# MyList = [10, 2, 9, 5, 3, 7, 4, 6, 8, 1]
Final_List = QuickSort(MyList, 0, len(MyList)-1)
print(Final_List)
