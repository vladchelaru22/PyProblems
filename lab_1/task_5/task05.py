def zig_zag(rows, cols):

    zig_zag_matrix = []

    ################### TO DO #########################
    zig_zag_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        j = i % (cols - 1)
        if i // (cols - 1) % 2 == 0:
            zig_zag_matrix[i][j] = 1
        else:
            zig_zag_matrix[i][cols - 1 - j] = 1
    ###################################################

    return zig_zag_matrix
