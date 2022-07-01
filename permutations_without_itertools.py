# A way to do permutations without repetition
def permutations_without_repetitions(elmnt):
    def helper_func(data):
        result = [] # Used to store the results
        if len(data) == 1: # Base case
            result.append(data[:])
        # The idea behind this method is to iterate over the elements of the list, remove an element
        # Get the permutations of of (list - 1) elements then add the removed element and add the results
        for i in range(len(data)):
            n = data[0]
            data.pop(0)
            perms = helper_func(data)
            for perm in perms:
                perm.append(n)
            data.append(n)
            result.extend(perms)
        return result
    final = []
    for sublist in helper_func(list(elmnt)):
        final.append("".join(sublist))
    return final


print(permutations_without_repetitions("123"))

# This is roughly equivalant to itertools.product implementation in python but modified to give permutations
# The idea behind it is to create lists, each with an element of data, then each time take that list and merge with it
# Another element of data until elements have the same length as data
def permutations_with_repetitions(data):
    l = len(data)
    result = [[]]
    groups = [list(data)] * l
    for i in groups:
        result = [x+[j] for x in result for j in i]
    result = ["".join(x) for x in result]
    print(result)
