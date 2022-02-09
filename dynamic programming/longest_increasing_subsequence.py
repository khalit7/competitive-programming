arr = [12,4,5,2,3,4,5,67,8]

n = len(arr)
dp = [1]*n

for i in range(n):
    best_candidate = 0
    for j in range(i-1,-1,-1):
        if arr[j] < arr[i]:
            best_candidate = max(best_candidate,dp[j])
    dp[i] = dp[i] + best_candidate

print(dp[-1])

print("time complexity = O(N^2)")
print("space complexity = O(N)")


# this problem can also be viewed as a longest common subsequence problem
# if we create a sorted version of the array, the longest common subsequence between the sorted array and the un sorted array should be the same as the longest common subsequence
'''
sorted_arr = sorted(arr)

n = len(arr)

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i-1] == sorted_arr[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max( dp[i-1][j],dp[i][j-1] )

print(dp[-1][-1])'''