# trapping the rainwater
# Optimal


def trappingRainwater(arr, n):
    left = 0
    right = n-1
    left_max = 0
    right_max = 0
    total_water = 0
    while(left <= right):
        if(arr[left] <= arr[right]):
            if(arr[left] >= left_max):
                left_max = arr[left]
            else:
                total_water += left_max-arr[left]
            left += 1
        else:
            if(arr[right] >= right_max):
                right_max = arr[right]
            else:
                total_water += right_max-arr[right]
            right -= 1
    return total_water
