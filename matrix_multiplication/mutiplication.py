def mutiplication(a, b):
    if len(a[0]) != len(b):
        raise "calulation cannot be done"
    # 1 2 3    4 5
    # 4 5 6    6 7
    # 7 8 9    7 8
    mat = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                mat[i][j] += a[i][k] * b[k][j]
    return mat