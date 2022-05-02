# Same as usual binary search
def binary_search(arr,elem):
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

# A new func to help applying Binary search on an sorted arr
def aux_fun(arr,elm):
    # Create a new list with sublists, each sublist has an element of arr and its index
    new_arr = [[y,x] for x,y in enumerate(arr)]
    # Sort the new list by the value of element
    new_arr.sort()
    # Binary search on sorted arr
    result = binary_search(sorted(arr),elm)
    # Now return the index of found element in original arr
    return new_arr[result][1]

print(aux_fun([9,-7,5,95,1,0],95))