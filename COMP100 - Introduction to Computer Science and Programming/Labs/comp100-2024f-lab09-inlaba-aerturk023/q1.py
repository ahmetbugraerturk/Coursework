def count_paths(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        return count_paths(m-1, n) + count_paths(m, n-1)


    