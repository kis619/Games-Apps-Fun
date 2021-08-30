def create_mapper(matrix):
    from collections import deque
    all_nums = deque(num for num in range(len(matrix) * len(matrix[0])))
    num_cel_mapper = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            num_cel_mapper[all_nums.popleft() + 1] = row, col

    return num_cel_mapper

number_cell_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

