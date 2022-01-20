'''
given tuples (a,b),(c,d)
valid operation 
1/(a+b,b)
2/ (a,a+b)

print yes if tuple (a,b) can be converted to (c,d)
print no other wise

constraints:

1<= a,b,c,d <1000
'''
a,b,c,d = list(map(int,input("enter a,b,c,d seperated by a single space \n").strip().split()))
n=1000
dp = [[False]*(n+1) for i in range(n+1)] 

dp [a][b] = True

for i in  range(1,n+1):
    for j in range(1,n+1):
        if dp[i][j] == True:
            if i+j < n+1:
                dp[i][i+j] = True
                dp[i+j][j] = True

ans = dp[c][d]

print(ans)


