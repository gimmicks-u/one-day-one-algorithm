def bin_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1
