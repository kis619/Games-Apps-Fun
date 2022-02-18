def indices_in_range(matrix, r, c):
    rows = len(matrix)
    cols = len(matrix[0])
    if 0 <= r <= rows - 1 and 0 <= c <= cols - 1:
        return True

    return False


def find_secondary_diagonal(position, matrix):
    r, c = position
    up_right_part_of_diagonal = []
    for row in range(max(len(matrix), len(matrix[0]))):
        r -= 1
        c += 1
        if indices_in_range(matrix, r, c):
            up_right_part_of_diagonal.append(matrix[r][c])

    r, c = position
    down_left_part_of_diagonal = []
    for row in range(max(len(matrix), len(matrix[0]))):
        r += 1
        c -= 1
        if indices_in_range(matrix, r, c):
            down_left_part_of_diagonal.append(matrix[r][c])

    r, c = position

    return down_left_part_of_diagonal[::1] + [matrix[r][c]] + up_right_part_of_diagonal


def find_primary_diagonal(position, matrix):
    r, c = position
    up_left_part_of_diagonal = []
    for row in range(max(len(matrix), len(matrix[0]))):
        r -= 1
        c -= 1
        if indices_in_range(matrix, r, c):
            up_left_part_of_diagonal.append(matrix[r][c])

    r, c = position
    down_right_part_of_diagonal = []
    for row in range(max(len(matrix), len(matrix[0]))):
        r += 1
        c += 1
        if indices_in_range(matrix, r, c):
            down_right_part_of_diagonal.append(matrix[r][c])

    r, c = position

    return up_left_part_of_diagonal[::-1] + [matrix[r][c]] + down_right_part_of_diagonal
