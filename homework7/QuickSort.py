def quickSort(x, l, r):
    
    if r <= l:
        return

    p = x[l]
    i = l
    j = r

    while i < j:
        while j >= l and x[j] > p:
            j = j - 1
        while i <= r and x[i] <= p:
            i = i + 1
        
        if i < j:
            x[i], x[j] = x[j], x[i]
    
    x[l], x[j] = x[j], x[l]
    
    quickSort(x, 0, j-1)
    quickSort(x, j+1, r)

import random

x = [random.randrange(10) for _ in range(10)]
print('unordered : ', x)
print()
quickSort(x, 0, len(x)-1)
print('ordered : ', x)
        

    