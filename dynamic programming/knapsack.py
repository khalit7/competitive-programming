values = [10,20,30,40,50,60,70]
weights = [1,3,1,4,5,6,8]
n = len(values)
capacity = 30

dp = [ [0]*(capacity+1) for _ in range(n+1)]

for i in range(1,n+1):
    ele_idx = i-1
    for j in range(1,capacity+1):
        if weights[ele_idx] <= j:
            dp[i][j] = max( dp[i-1][j] ,  values[ele_idx] +dp[i-1][j-weights[ele_idx]])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[-1][-1])