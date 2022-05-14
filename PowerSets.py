def genPowerSets(arr):
    # Base case
    if len(arr) == 0:
        return [[]]
    # Generate power set of arr without last elem
    smaller = genPowerSets(arr[:-1])
    # Last elem of arr
    extra = arr[-1:]
    new = []
    # Generate a copy of smaller with last elem
    for small in smaller:
        new.append(small+extra)
    # return power set of arr without last elem plus same power set with last elem
    return smaller + new