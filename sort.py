# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # implement your algorithm here
    # loop through the list
    for i in range(1, len(li)):
        # set the key to the current index
        key = li[i]
        # set j to the index before the current index
        j = i - 1
        # while j is greater than or equal to 0 and the key is less than the value at index j
        while j >= 0 and key < li[j]:
            # set the value at index j + 1 to the value at index j
            li[j + 1] = li[j]
            # decrement j
            j -= 1
        # set the value at index j + 1 to the key
        li[j + 1] = key

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
