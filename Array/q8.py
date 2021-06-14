# kadane's algo longest common subsequence


def maxSubArraySum(a, size):
    # Your code here
    max_sum = 0
    curr_sum = 0
    for i in range(size):
        curr_sum += a[i]
        if(curr_sum < 0):
            curr_sum = 0
        max_sum = max(max_sum, curr_sum)
    return max_sum
