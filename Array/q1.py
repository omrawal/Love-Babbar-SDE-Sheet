# reverse array


def reverseWord(s):
    # your code here
    n = len(s)
    if(n == 1):
        return s
    else:
        s = list(s)
        left = 0
        right = n-1
        while(left <= right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
