from Workshop1.play.mappers import *


def check_if_correct_input():
    sign_p1 = input(f"please choose a sign by typing \"X\" or \"O\": ")
    acceptable_signs = ["X", "x", "O", "o"]
    if not sign_p1 in acceptable_signs:
        print("You can only choose between 'X' and 'O'.")
        return check_if_correct_input()

    return sign_p1


def num_is_valid(number):
    if not number.isdigit():
        return False

    if not 0 < int(number) < 10:
        return False

    return True


def cell_is_free(number: int, matrix: list):
    r, c = number_cell_mapper[number]
    if matrix[r][c] == " ":
        return True

    return False


def someone_won_the_game(matrix, players_signs):
    if complete_primary_diagonal(matrix, players_signs):
        return True

    if complete_secondary_diagonal(matrix, players_signs):
        return True

    if complete_horizontal(matrix, players_signs):
        return True

    if complete_vertical(matrix, players_signs):
        return True

    return False


def complete_primary_diagonal(matrix, players_signs):
    diagonal = []
    for r in range(len(matrix)):
        diagonal.append(matrix[r][r])

    if three_consecutive(diagonal, players_signs):
        return True

    return False


def complete_secondary_diagonal(matrix, players_signs):
    diagonal = []
    for r in range(len(matrix)):
        diagonal.append(matrix[len(matrix) - 1 - r][r])

    if three_consecutive(diagonal, players_signs):
        return True

    return False


def complete_horizontal(matrix, players_signs):
    for row in matrix:
        if three_consecutive(row, players_signs):
            return True

    return False


def complete_vertical(matrix, players_signs):
    verticals = {f"Vertical{i}": [] for i in range(len(matrix))}

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            verticals[f"Vertical{c}"].append(matrix[r][c])

    for vertical in verticals.values():
        if three_consecutive(vertical, players_signs):
            return True

    return False


def three_consecutive(chars: list, players_signs: dict):
    for value in players_signs.values():
        if chars.count(value) == 3:
            return True

    return False


def full_board(matrix):
    flat_matrix = [matrix[j][i] for j in range(len(matrix)) for i in range(len(matrix))]
    if (flat_matrix.count("X") == 4 and flat_matrix.count("O") == 5) or \
            (flat_matrix.count("O") == 4 and flat_matrix.count("X") == 5):
        return True

    return False



