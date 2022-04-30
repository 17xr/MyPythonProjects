def zeros(n):
    count = 0
    k = 1
    while 5**k <= n:
        count += int(n/5**k)
        k += 1
    return count
