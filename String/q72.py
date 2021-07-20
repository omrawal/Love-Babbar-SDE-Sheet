# word break
# Given a string A and a dictionary of n words B,
#  find out if A can be segmented into a space-separated sequence of dictionary words.
# n = 12
# B = {"i", "like", "sam", "sung", "samsung", "mobile",
#      "ice", "cream", "icecream", "man", "go", "mango"}
# A = "ilike"
# Output: 1
# Explanation: The string can be segmented as "i like".


def wordBreak(line, dictionary):
    dp = [0]*len(line)
    for i in range(len(line)):
        for j in range(0, i+1):
            # print('checking',line[j:i+1])
            if(line[j:i+1] in dictionary):
                if(j > 0):
                    dp[i] += dp[j-1]
                else:
                    dp[i] += 1
    # print(dp)
    if(dp[len(line)-1] == 0):
        return False
    else:
        return True
