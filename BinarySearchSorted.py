# BINARY SEARCH USING RECURSION
# The main function
def binary_search(arr,elem):
    # A helper function
    def binary_search_helper(arr,left,right,elem):
        while left <= right:
            # the mid of the array
            mid = (left + right) // 2
            if arr[mid] == elem: # it's clear
                return mid
            # Since the middle element in the list is greater than the element we're looking for
            # Then the elem is in the  first half of array
            elif arr[mid] > elem:
                # Searching for element in first half
                return binary_search_helper(arr,left,mid - 1,elem)
            else:
                # Searching for elem in 2nd half since elem is greater than the mid elem of arr
                return binary_search_helper(arr,mid + 1,right ,elem)
        # return -1 if elem is not present in the list
        return -1
    # clear
    if len(arr) == 0:
        return  -1
    # Use the helper function in order to do the binary search using recursion
    else:
        return binary_search_helper(arr,0,len(arr),elem)

##############################
# BINARY SEARCH USING ITERATION
# Works the same as previous func


def binary_search1(arr,elem):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            right -= 1
        else:
            left += 1
    return -1