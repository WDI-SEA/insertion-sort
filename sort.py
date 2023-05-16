# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        print("i: ", "idx: ", i, "li[i]: ", li[i])
        while j >= 0 and key < li[j]:
            li[j + 1] = li[j]
            j -= 1
            print("     j: ", "idx: ", j, "li[j]: ", li[j])
        li[j + 1] = key


def weston_insertion_sort(li):
    # iterate up through the list, dragging down elements until they are in their proper place (either at the start of the list or next to a value to the left of it that is smaller)
    for current_index in range(len(li)):
        # for easy comparison, store the number that is being moved
        comparison_number = li[current_index]
        inner_index = current_index - 1
        while inner_index >= 0 and li[inner_index] > li[current_index]:
            # swap while these ar true
            li[inner_index], li[inner_index + 1] = li[inner_index + 1], li[inner_index]
            inner_index -= 1


# for testing
arr = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

li = [2,3,6,5,7,8,9,1]
print(li)
insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
print(li)

