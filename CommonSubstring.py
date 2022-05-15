def common(data):
    # Get the longest word from list
    longest = max(data,key=len)
    # Remove the longest word
    data.remove(longest)
    # A function to generate all substrings of a word
    substr = lambda _ : {_[i:j] for i in range(len(_)) for j in range(i+1,len(_)+1)}
    # All substrings of the longest word
    subs = substr(longest)
    # iterate over elements of data, generate all substrings of each word
    # then compare between generated substrings and those which belong to the longest word
    for word in data:
        subs.intersection_update(substr(word))
    # return longest word from all common substrings
    return max(subs,key=len)
