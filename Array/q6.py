# union and intersection of two sorted arrays
# union


def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i])
        i += 1

    while j < n:
        print(arr2[j])
        j += 1


# intersection
def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1
