# # use to check if the array is sorted
# def is_sorted(ls):
#     for i in range(len(ls) - 1):
#         if ls[i] > ls[i + 1]:
#             return False
#     return True


# def insertion_sort(li):
#     # implement your algorithm here
#     pass


# # for testing
# li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
#       41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

# insertion_sort(li)
# # should return True, because insertion sort is an in-place sort
# print(is_sorted(li))




# iterations = 0

# def sort_function(arr,swapped = True):
#     print(swapped, '🛑')
#     global iterations
    
#     if swapped == False:
#         print(arr)
#         return arr
#     else:
#         iterations += 1
#         swapped = False
#         for i in range(len(arr)-1):
#             # if arr[i] == arr[len(arr)-1]:
#             #     return sort_function(arr,swapped)
#             if arr[i] > arr[i+1]:  
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swapped = True
                
#                 #print(arr)
#             print(f'{i}, {swapped}')
#             if swapped == True:
#                 return sort_function(arr,swapped)

# print(sort_function([44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]), iterations)


def sort_function(arr):
    iterations = 0
    for i in range(1, len(arr)-1):
        temporary = i
        while arr[temporary-1] > arr[temporary] and temporary > 0:
            iterations+=1
            arr[temporary-1], arr[temporary] = arr[temporary], arr[temporary-1]
            temporary -= 1
    print(arr, iterations)

sort_function([44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4, 41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49])