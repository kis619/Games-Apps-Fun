def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(f"| {matrix[row][col]} ", end="")
        print("|")


def allot_signs(p1, p2, sign_p1):
    sign_p2 = "O" if sign_p1.upper() == "X" else sign_p2 = "X"
    player_signs = {p1: sign_p1.upper(), p2: sign_p2.upper()}

    return player_signs


def create_empty_matrix(matrix_size):
    matrix = []
    for row in range(matrix_size):
        line = []
        for c in range(matrix_size):
            line.append(" ")
        matrix.append(line)

    return matrix


def determine_order(counter, p1, p2):
    if counter % 2 == 1:
        player = p1

    else:
        player = p2

    return player


def create_matrix_with_nums(*args):  ### Not used in the programme but saved for future reference
    rows = args[0]
    cols = args[-1]
    numbers = [num for num in range(rows * cols)]
    matrix = []
    for row in range(rows):
        line = []
        for c in range(cols):
            line.append(numbers[0] + 1)
            numbers = numbers[1:]
        matrix.append(line)

    return matrix