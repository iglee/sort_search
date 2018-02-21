def binary_search(A, x, low, high):
    if low < high:
        middle = 1+(high - low)/2
        if A[middle] == x:
            return middle
        if A[middle] > x:
            high = middle - 1
            return binary_search(A, x, low, high)
        if A[middle] < x:
            low = middle + 1
            return binary_search(A, x, low, high)
    else:
        print "element not found"

def bubble_sort(items):
    switch = False
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
            switch = True
    if switch == False:
        return items
    else:
        return bubble_sort(items)

def selection_sort(items):
    for i in range(len(items)-1):
        min_idx = i
        for j in range(i, len(items)):
            if min_idx > items[j]:
                min_idx = j
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
    return items
