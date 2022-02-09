def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]






arr = list(map(int,input("enter arrays values seperated by space \n").strip().split()))

bubble_sort(arr)

print("here is the sorted array: ")
print(arr)

print("time complexity O(N^2)")
print("space complexity O(1)")