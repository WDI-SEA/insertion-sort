# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # for loop that will iterate through 'li' starting from the second element(index 1) to the last element. 'i' will keep track of the current position in the list being considered
    for i in range(1, len(li)):
        # intialize j to i, so that j will keep track of the current position in the list being considered
        j = i
        # while loop that continues until either j is no longer greater than 0 or li[j-1] is no longer greater than li[j]. The first condition ensures that the loop does not go beyond the first element of the list, while the second condition ensures that the elements are in the correct order
        while j > 0 and li[j - 1] > li[j]:
            # this line swaps the elements at positionsj-1 and j in the list
            li[j - 1], li[j] = li[j], li[j - 1]
            # this line decrements the value of j by 1. This moves j one position to the left in the list and prepares it for the next iteration of the while loop
            j -= 1


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
