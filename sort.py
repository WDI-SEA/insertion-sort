# use to check if the array is sorted
iterations = 0
def is_sorted(ls):

    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # implement your algorithm here
    global iterations 
    for i in range(1, len(li)):
        iterations += 1
        currentvalue = li[i]
        position = i

        while position > 0 and li[position - 1] > currentvalue:
            li[position] = li[position - 1]
            position = position - 1
        
        li[position] = currentvalue


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(f'List was {len(li)}, iterations to sort: {iterations}')
print(is_sorted(li))
print(li)
