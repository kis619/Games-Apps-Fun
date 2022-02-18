from play.matrix_diagonals import *


def check_name_recursion(player: str, player2) -> str:
    name = input(f"{player} please choose a name: ")
    if name == player2:
        print("Player one already took this name.\n"
              "Please choose a different one.")
        return check_name_recursion(player, player2)

    requirements = "The name must contain at least two characters and cannot begin or end with a space."
    if len(name) < 2 or name.startswith(" ") or name.endswith(" "):
        print(requirements)

        if len(name) < 2:
            print("Your name is too short.")

        if name.startswith(" "):
            print("Your name starts with a space.")

        if name.endswith(" "):
            print("Your name ends with a space.")

        name = check_name_recursion("Give it a thought and", player2)

    return name


def check_name(name: str) -> str:
    requirements = "The name must contain at least two characters and cannot begin or end with a space."
    while len(name) < 2 or name.startswith(" ") or name.endswith(" "):
        print(requirements)

        if len(name) < 2:
            print("Your name is too short.")

        if name.startswith(" "):
            print("Your name starts with a space.")

        if name.endswith(" "):
            print("Your name ends with a space.")

        name = input("PLease choose a different name: ")

    return name


def check_if_number_and_if_within_limits(char: str, limits: tuple) -> int:
    while not char.isdigit():
        char = input("This is not a number.\n"
                     "Please pick a number: ")

    while not limits[0] <= int(char) <= limits[1]:
        char = input(f"Please choose a number in the range ({limits[0]}-{limits[1]}): ")

    return int(char)


def check_if_column_full(column, matrix):
    while not matrix[0][column] == 0:
        print("This column is full.")
        column = input("Please choose another one: ")
        column = check_if_number_and_if_within_limits(column, (0, len(matrix[0]))) - 1

    return column


def check_y_n_response(response):
    positive_responses = ["y", "Y", "yes", "YES", "Yes", "да", "ДА"]
    negative_responses = ["n", "N", "no", "NO", "No", "не", "НЕ"]
    while response not in positive_responses and response not in negative_responses:
        response = input("I do not speak human.\n"
                         "Please type 'Y' or 'N': ")

    return "Yes" if response in positive_responses else "No"


def check_if_game_over(player: str, last_move: tuple, matrix: list, play_again):
    game_over = False
    if someone_won(last_move, matrix):
        game_over = True
        print(f"{player} won!\n"
              f"Congratulations, {player}, you are the best!")

    elif stalemate(matrix):
        game_over = True
        print(f"Game over.\n"
              f"No one won!")

    if game_over:
        retry = input("Do you wanna play again? (Y/N): ")
        retry = check_y_n_response(retry)
        if retry == 'Yes':
            play_again()
        else:
            print("Okay, bye!")
            exit(0)


def stalemate(matrix: list):
    for row in matrix:
        if row.count(0):
            return False

    return True


def someone_won(position, matrix):
    r, c = position
    four_consecutive_tokens = str(matrix[r][c]) * 4
    row = ''.join(str(el) for el in matrix[r])
    column = ''.join([str(matrix[i][c]) for i in range(len(matrix))])
    primary_diagonal = ''.join(str(el) for el in find_primary_diagonal(position, matrix))
    secondary_diagonal = ''.join(str(el) for el in find_secondary_diagonal(position, matrix))

    if any((
            four_consecutive_tokens in row,
            four_consecutive_tokens in column,
            four_consecutive_tokens in primary_diagonal,
            four_consecutive_tokens in secondary_diagonal
    )):
        return True

    return False














