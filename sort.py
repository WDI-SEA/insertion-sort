
# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return ls


def insertion_sort(li):
    #This is the function definition for insertion_sort, which will sort an input list li in-place.
    for i in range(1, len(li)):
        #Loop over ever element but index 0 because it will already be sorted
        key = li[i]
        #current value set to key
        j = i-1
        #set j as the last value sorted
        while j >=0 and key < li[j] :
                #start of the while loop as long as j is a valid number
                li[j+1] = li[j]
                #shifts li[j] to the right
                j -= 1
                #moves j one to the right for next iteration of while
        li[j+1] = key
        #once the while loop is done insert key into right spot
    pass


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

insertion_sort(li)
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))



















#CLONED WRONG ONE IN LAB YESTERDAY IGNORE THIS
# def bubble_sort(numbers):
#     length = len(numbers)
#     for i in range(length - 1):
#         for j in range(length - 1 - i):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     return numbers
        
# print(bubble_sort(numbers))



# def bubble_sort(numbers):
#     length = len(numbers)
#     for i in range(numbers):

# def bubble_sort(numbers):
#     length = len(numbers)

#     if length <= 1:
#         return numbers

#     for i in range(length-1):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

#     return bubble_sort(numbers[:-1]) + [numbers[-1]]

# print(bubble_sort(numbers))