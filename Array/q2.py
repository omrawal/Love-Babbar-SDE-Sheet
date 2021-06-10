# find min and max in array


def findMinMax(arr):
    min_ele = arr[0]
    max_ele = arr[0]
    for i in arr:
        min_ele = min(min_ele, i)
        max_ele = max(max_ele, i)
    return (min_ele, max_ele)
