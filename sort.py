# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True

def swap(i, j):
    li2[i], li2[j] = li2[j], li2[i]

def insertion_sort(li2):
    for i in range(1, len(li2)):
        print(f'this is for loop: {li2}')
        j = i
        while j > 0 and li2[j] < li2[j - 1]:
            swap(j, j - 1)
            j -= 1
            print(f'this is while loop: {li2}')


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

li2 = [12, 1, 32, 23, 21, 8]

insertion_sort(li2)
print(li2)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li2))
