arr = list(map(int,input("enter arrays values seperated by space \n").strip().split()))

dp = 1 

for ele in arr:
    dp |= dp<<ele

print("all possible sums are : ")
for i in range(1,sum(arr)+1):
    if dp>>i & 1:
        print(i,end=" ")