# Implementing Radix Sort using Python
# Date: 01/04/2021
# Author: Pranav H. Deo

import numpy as np


def RadixSort(L, ord):
    Reloader_List = []
    temp = []
    for i in range(0, 10):
        Reloader_List.append([])
    for i in range(0, ord):
        print('Iteration ', i, ' : ', L)
        for ele in L:
            n = int((ele / np.power(10, i)) % 10)
            Reloader_List[n].append(ele)
        for lst in Reloader_List:
            if len(lst) > 0:
                for e in lst:
                    temp.append(e)
        L = temp
        temp = []
        for k in range(0, 10):
            Reloader_List[k] = []
    return L


# MyList = [102, 209, 90, 1, 458, 923, 9, 48, 20]
MyList = np.random.randint(0, 500, 100)
order = 3
Final_List = RadixSort(MyList, order)
print('\n', Final_List)