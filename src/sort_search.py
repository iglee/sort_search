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
