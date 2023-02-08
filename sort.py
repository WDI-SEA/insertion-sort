# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


    # implement your algorithm here

## == ## PSEUDOCODE: ## == ##

## variables?

# initial sorted range is just array[0]

# check array[i] against sorted_range (array[0] through array[i-1]):

    # if array[i] > last index of sorted_range:
        # leave it, and open the sorted_range to include array[i]
        # move to next index

    # if array[i] < last index of sorted_range:
        # swap array[i] with array [i-1]
        # open sorted range to new array[i]

   # run is_sorted(array) to check if it's finished


initial_array = [2,9,4,6,1,3]

def insertion_sort(array):

    # check array[i] against sorted_range (array[0] through array[i-1]):
    for i in range(len(array)-1):
        if i == (len(array)):
            print('done sorting!')
            return True
        # if array[i] > last index of sorted_range:
        if array[i+1] >= array[i]:
            print('the number is in its proper place')
            # move to next index

        # if array[i] < last index of sorted_range:
        else: #if array[i+1] < array[i]:

            while_loop_running = True

            while while_loop_running:
        
                if array[i+1] < array[i]:
                    print('it needs to be swapped with the number to its right')
            # swap array[i] with array [i-1]
                    array[i], array[i+1] = array[i+1], array[i]
                    continue
                else:
                    print('it is smaller than the number to its right and in proper place')
                    print(array)
                    while_loop_running = False
                    # return
    print(array)

insertion_sort(initial_array)
   # run is_sorted(array) to check if it's finished


# for testing
test_array = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

# insertion_sort(test_array)
# # should return True, because insertion sort is an in-place sort
# print(is_sorted(test_array))


    