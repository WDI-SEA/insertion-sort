# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # iterate through list and move elements down if they are less than the element to the left
    for index in range(len(li)):
        # current number for comaprisons
        current_number = li[index]
        # use while loop to go back down the list
        cur_pos = index - 1
        while cur_pos >= 0 and current_number < li[cur_pos]:
            # swap the values
            li[cur_pos], li[cur_pos + 1] = li[cur_pos + 1], li[cur_pos]
            cur_pos -= 1


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
