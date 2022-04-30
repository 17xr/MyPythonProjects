def tribonacci(signature, n):
    res = []
    if n == 0:
        return res
    if n <= 3:
        return [signature[x] for x in range(0,n)]
    res = signature[:]
    for x in range(3,n):
        res.append(sum(res[-1:-4:-1]))
    return res
