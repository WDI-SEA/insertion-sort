# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # implement your algorithm here
    # create insertion sort algorithm
    for i in range(1, len(li)): # start from 1 because 0 is already sorted
        key = li[i] # key is the value we want to insert
        j = i - 1 # j is the index of the last element in the sorted array
        while j >= 0 and key < li[j]: # while j is not out of range and key is smaller than the last element in the sorted array
            li[j + 1] = li[j] # move the last element in the sorted array to the right
            j -= 1 # move j to the left
        li[j + 1] = key # insert the key to the right of j




# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
print("Sorted list:", li)
