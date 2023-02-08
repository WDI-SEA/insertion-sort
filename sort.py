# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # implement your algorithm here

    for i in range(0, len(li)):
        current_value = li[i]
        for j in range(i-1, -1, -1):
            if current_value < li[j]:
                li[j], li[j+1] = li[j+1], li[j]
            else: 
                break

    # for current_index, current_value in enumerate(li):
    #     inner_loop_index = current_index -1
    #     while inner_loop_index >= 0 and current_value < li[inner_loop_index]:
    #         li[inner_loop_index], li[inner_loop_index + 1] = li[inner_loop_index +1], li[inner_loop_index]
    #         inner_loop_index -= 1

    # for i in range(len(li)-1):
    #     j = i
    #     while li[j-1] > li[j] and j > 0:
    #         li[j-1], li[j] = li[j], li[j-1]
    #         j -= 1


    
    pass


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
