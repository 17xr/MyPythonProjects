def find_uniq(arr):
    arr.sort()
    if (arr[0] != arr[len(arr)-1] and arr[0] != arr[len(arr)-2]):
        return arr[0]
    else:
        return arr[len(arr)-1]
#########################################
def find_uniq(arr):
    x, y = set(arr)
    return x if arr.count(x) == 1 else y
