# The selection sorting algorithm is based on choosing the first element of the list then compare it with other elements
# to check if it's the smallest one, it that's the case then we put that element at the beginning of the list
# then we take the second element and continue to get a nice sorted array
def selection_sort(arr):
    # index of first element
    start = 0
    while start != len(arr):
        # check if the chosen element is the smallest in the array
        for i in range(start, len(arr)):
            # when we find a smaller element we flip them
            if arr[i] < arr[start]:
                arr[i], arr[start] = arr[start], arr[i]
        # since we got the smallest element, we move to the next one
        start += 1
    # return the sorted array
    return arr

# ===========================================================================
# The bubble sorting algo is based on comparing each 2 adjacent elements
# then make sure elem with index (i) is smaller than its adjacent with index (i+1)
# we continue iterating over the array until it's sorted


def bubble_sort(arr):
    # a flag set to false
    check = False
    # while the sorting is not done yet
    while not check:
        # set the flag to True
        check = True
        # iterate over the array
        for i in range(1, len(arr)):
            # if 2 elements are not sorted, we flip them then set the flag to false
            if arr[i-1] > arr[i]:
                check = False
                arr[i - 1], arr[i] = arr[i], arr[i-1]
    # the algo will continue iterating over the array, till everything is done then it returns the sorted arr
    return arr

# ===========================================================================
# The merge and sort algo is based on dividing the array into 2 smaller array, continue doing that until
# we get either an array with length 0 or 1, then merge and sort each 2 small arrays till we get a nice sorted array

# A helper function to merge 2 arrays into a big sorted one


def merge_sort(left, right):
    result = []
    i, j = 0, 0

    # compare elements with same index of the 2 arrays and take the smallest
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # copy the rest of elements of 'left' array
    while i < len(left):
        result.append(left[i])
        i += 1

    # copy the rest of elements of 'right' array
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# the main function
def merge(arr):
    # if the list has 1 element, or it's empty then simply return a copy of it
    if len(arr) < 2:
        return arr[:]
    # if not then divide it
    else:
        # mid index
        mid = len(arr) // 2
        # well it's kinda hard to understand this (at least to me)
        # we will use recursion to sort the first half using the same marge and sort algo
        # the same for the second half
        prefix = merge(arr[:mid])
        suffix = merge(arr[mid:])
        # we will then merge both parts while sorting them
        return merge_sort(prefix, suffix)
