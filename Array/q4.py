# sort 0,1,2


def msort(arr):
    n = len(arr)
    if(n <= 1):
        return arr
    else:
        left = 0
        curr = 0
        right = n-1
        while(curr <= right):
            if(arr[curr] == 0):
                arr[curr], arr[left] = arr[left], arr[curr]
                curr += 1
                left += 1
            elif(arr[curr] == 2):
                arr[curr], arr[right] = arr[right], arr[curr]
                right -= 1
            else:
                curr += 1
    return arr


arr = [0, 1, 0]
print(msort(arr))
