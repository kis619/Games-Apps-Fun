from Workshop1.play.helpers import *
from Workshop1.play.checks import *


def setup():
    p1_name = input("PLayer one name: ")
    p2_name = input("PLayer two name: ")
    sign_p1 = check_if_correct_input()
    players_signs = allot_signs(p1_name, p2_name, sign_p1)
    matrix_visual = [
        "| 1 | 2 | 3 |",
        "| 4 | 5 | 6 |",
        "| 7 | 8 | 9 |"
    ]
    print("This is the numeration of the board: ")
    print(*matrix_visual, sep="\n")
    play(p1_name, p2_name, players_signs)


def play(p1_name, p2_name, players_signs):
    matrix = create_empty_matrix(3)
    someone_won = False
    stalemate = False
    turn_counter = 1

    while not stalemate and not someone_won:
        player = determine_order(turn_counter, p1_name, p2_name)
        number = input(f"{player} please choose a free cell by typing the corresponding number: ")

        if not num_is_valid(number):
            print("Please enter a valid number.")
            continue

        if not cell_is_free(int(number), matrix):
            print("This cell is taken. Please choose a free cell.")
            continue

        r, c = number_cell_mapper[int(number)]
        matrix[r][c] = players_signs[player]
        print_matrix(matrix)
        someone_won = someone_won_the_game(matrix, players_signs)
        stalemate = full_board(matrix)
        turn_counter += 1

    if someone_won:
        print(f"Game over.\n"
              f"{player} won!")

    else:
        print("It's a tie! You are both winners.\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "Or both losers....")







