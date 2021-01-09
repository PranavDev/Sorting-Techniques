# Implementing Bubble Sort using Python
# Date: 01/03/2021
# Author: Pranav H. Deo

import numpy as np


def BubbleSort(L):
    temp = 0
    for i in range(0, len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L


MyList = np.random.randint(0, 500, 100)
Final_List = BubbleSort(MyList)

print(Final_List)
