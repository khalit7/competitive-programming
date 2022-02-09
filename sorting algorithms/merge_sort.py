def merge(arr,low,high,mid):
    
    l_copy = arr[low:mid+1]
    r_copy = arr[mid+1:high+1]

    l_index = 0
    r_index = 0

    sorted_index = low

    while l_index < len(l_copy) and r_index < len(r_copy):
        if l_copy[l_index] < r_copy[r_index]:
            arr[sorted_index] = l_copy[l_index]
            l_index += 1
        else:
            arr[sorted_index] = r_copy[r_index]
            r_index += 1

        sorted_index += 1

    while l_index < len(l_copy):
        arr[sorted_index] = l_copy[l_index]
        sorted_index += 1
        l_index += 1

    while r_index < len(r_copy):
        arr[sorted_index] = r_copy[r_index]
        sorted_index += 1
        r_index += 1

    
def merge_sort(arr,low,high):
    if low < high:

        mid = (low+high)//2

        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,high,mid)


arr = list(map(int,input("enter arrays values seperated by space \n").strip().split()))

merge_sort(arr,0,len(arr)-1)

print("here is the sorted array: ")
print(arr)
print("time complexity O(N*LogN)")
print("space complexity O(N)")