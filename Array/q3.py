# find kth smallest


import heapq


def kthSmallest(self, arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    return arr[k-1]

# O(n+ k logn)


class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heapq.heapify(arr)
        for i in range(k-1):
            heapq.heappop(arr)
        return heapq.heappop(arr)
