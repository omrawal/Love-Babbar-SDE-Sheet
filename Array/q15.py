# next permutation
def reverse(nums, start, end):
    while(start <= end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


def optimal(nums):
    n = len(nums)
    i = n-2
    while(i >= 0 and nums[i] > nums[i+1]):
        i -= 1
    ind1 = i
    if(ind1 >= 0):
        j = n-1
        while(nums[j] <= nums[i]):
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return reverse(nums, i+1, n-1)


print(optimal([5, 3, 1, 4, 2]))
