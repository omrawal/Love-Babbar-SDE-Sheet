# first and last occurance
#  0 1 2 3 4 5 6 7
# [1,2,3,4,5,5,5]
#        f
#                l
# X = 5


def find(arr, n, x):
    # code here
    left = 0
    right = n-1
    while(left <= right):
        mid = (left+(right-left)//2)
        if(arr[mid] == x):
            # find first and last occurance
            first = mid
            last = mid
            while(first >= 0 and arr[first] == x):
                first -= 1

            while(last < n and arr[last] == x):
                last += 1

            return [first+1, last-1]

        elif(arr[mid] < x):
            left = mid+1
        else:
            right = mid-1
    return [-1, -1]


arr = [1, 2, 3]
x = 5
print(find(arr, len(arr), x))
