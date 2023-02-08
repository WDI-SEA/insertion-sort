# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True

iterations = 0
def insertion_sort(li):
    global iterations
    
    for i in range(len(li)):
        # keep track of the current number for comparisons
        current_value = li[i]
        for j in range(i - 1, -1, -1):
            iterations += 1
            if current_value < li[j]:
                li[j], li[j + 1] = li[j + 1], li[j]
            else:
                break


def bubble_sort(unsorted_list):
    global iterations
    # loop over the list until one iteration has completed without making any changes
    made_swap = True 

    while made_swap:
        # stop further iterations unless a swap is made
        made_swap = False
        # iterate the whole array
        for i in range(len(unsorted_list) - 1):
            iterations += 1 
            # check neighboring values and swap them if the current one is greater than
            if unsorted_list[i] > unsorted_list[i + 1]:
                # make a swap here
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                made_swap = True

# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

#insertion_sort(li)
bubble_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
print(iterations)
print(len(li))
