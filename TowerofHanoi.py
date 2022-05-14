def tower_of_honai(n,start,mid,end):
    # Base case
    if n == 0:
        return
    # move top (n-1) disks from rod 1 to 2
    tower_of_honai(n-1,start,end,mid)
    # move largest disk from rod 1 to 3
    print("Moved disk number {} from rod {} to rod {}".format(n,start,end))
    # move top (n-1) from rod 2 to rod 3
    tower_of_honai(n-1,mid,start,end)