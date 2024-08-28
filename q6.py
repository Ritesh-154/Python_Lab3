def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = temp
    return arr


def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]   
                j += 1
                k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print("Enter 1 for bubble sort")
print("Enter 2 for selection sort")
print("Enter 3 for insertion sort")
print("Enter 4 for merge sort")
a=int(input("Enter option : "))
if a == 1:
    sorted_arr = bubble_sort(arr)
elif a == 2:
    sorted_arr = selection_sort(arr)
elif a == 3:
    sorted_arr = insertion_sort(arr)
elif a == 4:
    sorted_arr = merge_sort(arr)
else:
    print("Option not matched")
print("Sorted array is:",sorted_arr)