# use to check if the array is sorted
def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def insertion_sort(li):
    # implement your algorithm here
    # First we need to set up an iteration
    for i in range(len(li)):
        # ^ This should iterate through the whole length of the li
        # Next we need a way to see the algorithms current position through the list
        position = li[i]
        # ^This gives us the position/index of the algorithm
        # Now we need a way to move through the algorithm
        moved = i - 1
        # ^ This is our secondary list counter
        # Now here is the hard part
        # We need to set up the actual algorithm
        # We keep looping until the current value is in its correct position in the list
        while moved >= 0 and li[moved] > position:
            # Shift the elements one ro the right to make room for the value
            li[moved + 1] = li[moved]
            # Decrement the counter for the inner loop, so we can restart the algorithm
            moved -= 1
        # Insert the current value into its correct position
        li[moved + 1] = position
    # Returns the li back to itself allowing for the continual sort until finished
    return li


# for testing
li = [44, 41, 35, 34, 7, 8, 44, 38, 28, 44, 16, 31, 13, 31, 42, 19, 2, 47, 32, 17, 14, 27, 30, 4,
      41, 39, 37, 30, 42, 43, 10, 3, 48, 16, 11, 47, 9, 40, 22, 23, 9, 2, 35, 6, 7, 5, 45, 42, 24, 49]

print(insertion_sort(li))
# should return True, because insertion sort is an in-place sort
print(is_sorted(li))
