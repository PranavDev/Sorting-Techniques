# Implementing Insertion Sort using Python
# Date: 01/03/2021
# Author: Pranav H. Deo

import numpy as np


def InsertionSort(L):
    temp = 0
    for j in range(1, len(L)):
        i = j - 1
        b = j
        while i >= 0:
            if L[j] < L[i]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                j -= 1
            i -= 1
        j = b
    return L


MyList = np.random.randint(0, 500, 100)
# MyList = [9, 6, 5, 3, 0, 8, 4, 2, 7, 1]
Final_List = InsertionSort(MyList)

print(Final_List)