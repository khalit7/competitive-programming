from random import randrange


def heapify(arr,n,i):
    largest = i
    
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]

        heapify(arr,n,largest)


def build_heap(arr):
    n = len(arr)

    for i in range(n//2 -1 ,-1,-1):
        heapify(arr,n,i)

def get_element(heap): # we dont need this to do the sorting ! I wrote it here just for completion
    last_index = len(heap)-1
    heap[0],heap[last_index] = heap[last_index],heap[0]
    element = heap.pop()

    return element

def add_element(heap,element): # we dont need this to do the sorting ! I wrote it here just for completion
    heap.append(element)
    last_index = len(heap)-1
    root = (last_index-1)//2
    while True :
        heapify(heap,len(heap),root)
        if root == 0:
            break
        else:
            root = (root-1)//2

def heap_sort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)


arr = list(map(int,input("enter arrays values seperated by space \n").strip().split()))

heap_sort(arr)

print("here is the sorted array: ")
print(arr)

print("time complexity O(N*LogN)")
print("space complexity O(1)")