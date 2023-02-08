# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # iterate the list once in an outer loop
    for current_index, current_value in enumerate(li):
        # inner loop that iterates backwards and places items where they need to be
        inner_loop_index = current_index - 1
        while inner_loop_index >= 0 and current_value  < li[inner_loop_index]:
            li[inner_loop_index], li[inner_loop_index + 1] = li[inner_loop_index + 1], li[inner_loop_index]
            inner_loop_index -= 1
            # check if the current value is less than than the one to the right
                # if so swap, if not break
            # if we bump into index 0, stop and place the current value at 0


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
print(li)



