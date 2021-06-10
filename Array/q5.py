# move all negative to right

# O(nlogn)


def brute(arr):
    arr.sort()
    return arr

# O(n)


def optimal(arr):
    n = len(arr)
    left = 0
    curr = 0
    while(curr < n):
        if(arr[curr] < 0):
            arr[curr], arr[left] = arr[left], arr[curr]
            curr += 1
            left += 1
        else:
            curr += 1
    return arr


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(optimal(arr))
