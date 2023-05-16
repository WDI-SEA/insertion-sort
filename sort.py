# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True

iterations = 0

def insertion_sort(li):
    global iterations
    for i in range(1, len(li)):
        key = li[i]
        j = i -1
        print(f"i: {i}, j: {j}")
    # Compare key with each element on the left of it until an element smaller than it is found
    # For descending order, change key<array[j] to key>array[j].  
        while j >= 0 and key < li[j]:
            iterations += 1
            li[j + 1] = li[j]
            j = j -1
    # Place key at after the element just smaller than it.
    li[j + 1] = key
    print(f"iterations: {iterations}")

def insertion_sort(arr):
    global iterations
    # loop through array starting at 1 till len of arr
    for i in range(1, len(arr)):
        print(arr)
        # get current item
        item = arr[i]
        # get index of previous item
        j = i - 1
        #  check if current > item
        while j >= 0 and arr[j] > item:
            iterations += 1
            # shift current up one space
            arr[j+1] = arr[j]
            # move left to check next
            j -= 1
        
        # When finished shifting elements place item in its correct position
        arr[j+1] = item
    print (f"iterations: {iterations}")
    return arr
# for testing
li = [41, 7, 35, 44, 8, 34, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
