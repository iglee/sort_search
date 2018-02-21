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
