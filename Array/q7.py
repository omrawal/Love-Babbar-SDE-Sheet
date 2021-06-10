# clockwise cyclically rotate array by 1


def rotate(arr, n):
    k = arr[-1]
    i = n-1
    while(i > -1):
        arr[i] = arr[i-1]
        i -= 1
    arr[0] = k
    return arr
