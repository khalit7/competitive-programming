import random

def partition(arr,low,high):

    pivot = random.randrange(low,high+1)

    arr[pivot] ,arr[high] = arr[high],arr[pivot]

    i = low - 1

    for j in range(low,high):
        if arr[j] < arr[high]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quick_sort(arr,low,high):
    if low < high : 
        p = partition(arr,low,high)
        quick_sort (arr,low,p)
        quick_sort (arr,p+1,high)

arr = list(map(int,input("enter arrays values seperated by space \n").strip().split()))

quick_sort(arr,0,len(arr)-1)

print("here is the sorted array: ")
print(arr)

print("time complexity O(N*LogN)")
print("space complexity O(1)")
