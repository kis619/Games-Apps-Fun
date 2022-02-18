from play.checks import *


def setup():
    player1 = input(f"Player one please choose a name: ")
    player1 = check_name(player1)
    player2 = check_name_recursion("PLayer two", player1)
    print("Good job!")
    players_tokens = {player1: "1", player2: "2"}
    print(f"{player1} will be playing with '1'.\n"
          f"{player2} will be playing with '2'.")
    confirmation = input("Ready? (Y/N): ")
    confirmation = check_y_n_response(confirmation)
    if confirmation == "No":
        print("Ok, byeeee!")
        exit(0)

    rows, columns = pick_a_size()
    print("The field is all set up.")
    print()
    empty_matrix = create_matrix(rows, columns)
    print_matrix(empty_matrix)
    print()
    print(f"{player1}, begin please.\n")
    play(empty_matrix, players_tokens, player1, player2)


def play(matrix, players_tokens, player1, player2):
    next_player = player1
    curr_player = player2

    while True:
        curr_player, next_player = next_player, curr_player
        column = input(f"Type the number of the chosen column (1 - {len(matrix[0])}): ")
        column = check_if_number_and_if_within_limits(column, (1, len(matrix[0]))) - 1
        column = check_if_column_full(column, matrix)
        matrix, row = place_token_at_lowest_empty_spot(column, players_tokens[curr_player], matrix)
        print_matrix(matrix)
        last_move = row, column
        check_if_game_over(curr_player, last_move, matrix, setup)
        print(f"{next_player}, it's your turn.")


def place_token_at_lowest_empty_spot(column, token, matrix):
    for row in range(len(matrix) - 1, -1, -1):
        if matrix[row][column] == 0:
            matrix[row][column] = int(token)
            break

    return matrix, row


def create_matrix(*args):
    rows = args[0]
    columns = args[-1]
    matrix = []
    for r in range(rows):
        row = [0 for c in range(columns)]
        matrix.append(row)

    return matrix


def pick_a_size():
    default = 6, 7
    from play.mappers import sizes
    choice = input("The default size of the playing field is '6x7' (6 rows, 7 columns)\n"
                   "To continue with the default playing field enter '0';\n"
                   "to choose a different size enter '1': ")
    choice = check_if_number_and_if_within_limits(choice, (0, 1))
    if choice == 0:
        return default

    further_choice = input("PLease choose a size by typing the corresponding number.\n"
                           "1 for size 4x5,\n"
                           "2 for size 5x6,\n"
                           "3 for size 7x8,\n"
                           "4 for size 7x9,\n"
                           "5 for size 7x10,\n"
                           "6 for size 8x8,\n"
                           "7 for custom size.\n"
                           "Your answer: ")

    further_choice = check_if_number_and_if_within_limits(further_choice, (1, 7))
    if further_choice == 7:
        rows = input("Number of rows (4-10): ")
        rows = check_if_number_and_if_within_limits(rows, (4, 10))
        columns = input("Number of columns (4-10): ")
        columns = check_if_number_and_if_within_limits(columns, (4, 10))
        return rows, columns

    return sizes[further_choice]


def print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(f"| {matrix[row][col]} ", end="")
        print("|")
