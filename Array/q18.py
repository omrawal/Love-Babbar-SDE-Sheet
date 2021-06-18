# Count pairs with given sum
# INCOMPLETE


def getPairsCount(arr, n, k):
    if(n < 2):
        return 0
    pairs = 0
    count_dict = {}
    for i in arr:
        if(i in count_dict):
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    for i in arr:
        # count_dict[i]-=1
        target = k-i
        pairs += count_dict[target]
        # count_dict[i]+=1

    return pairs//2
