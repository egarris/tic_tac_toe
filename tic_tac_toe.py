def main():
    cells = list('         ')
    turn = 0
    print_state(cells)
    while True:
        coords = list(input('Enter the coordinates: ').replace(' ', ''))
        make_move(coords, cells, turn)
        analyze_game(cells)
        turn += 1


def print_state(game):
    print("---------\n" + "| " + game[0] + " " + game[1] + " " + game[2] + " |"
          + "\n| " + game[3] + " " + game[4] + " " + game[5] + " |"
          + "\n| " + game[6] + " " + game[7] + " " + game[8]
          + " |" + "\n---------")


def make_move(user_input, game, turn):
    # Check that coordinates are integers
    try:
        user_input = [int(coord) for coord in user_input]
    except ValueError:
        print('You should enter numbers!')
    # Check that each coordinate is within range
    while user_input[0] not in [1, 2, 3] or user_input[1] not in [1, 2, 3]:
        print('Coordinates should be from 1 to 3!')
        user_input = list(input('Enter the coordinates: ').replace(' ', ''))
        try:
            user_input = [int(coord) for coord in user_input]
        except ValueError:
            print('You should enter numbers!')
    # Map coordinate array to game array
    user_input = int(str(user_input[0]) + str(user_input[1]))
    grid = [11, 12, 13, 21, 22, 23, 31, 32, 33]
    idx = grid.index(user_input)
    # Check if cell at coordinates is occupied
    while game[idx] == 'X' or game[idx] == 'O':
        print('Cell is occupied! Choose another one!')
        user_input = list(input('Enter the coordinates: ').replace(' ', ''))
        try:
            user_input = [int(coord) for coord in user_input]
            user_input = int(str(user_input[0]) + str(user_input[1]))
            grid = [11, 12, 13, 21, 22, 23, 31, 32, 33]
            idx = grid.index(user_input)
        except ValueError:
            print('You should enter numbers!')
    # Set value of empty cell
    if turn % 2 == 0:
        game[idx] = 'X'
    else:
        game[idx] = 'O'
    print_state(game)


def analyze_game(game):
    # Slice rows and columns for analysis
    rows = [[game[0], game[1], game[2]], [
        game[3], game[4], game[5]], [game[6], game[7], game[8]]]
    cols = [[game[0], game[3], game[6]], [
        game[1], game[4], game[7]], [game[2], game[5], game[8]]]
    x_amt, o_amt = 0, 0
    X_WINS, O_WINS = ['X', 'X', 'X'], ['O', 'O', 'O']
    # Ensure X's or O's don't outnubmer each other by 2 or more
    for mark in game:
        if mark == 'X':
            x_amt += 1
        if mark == 'O':
            o_amt += 1
    if abs(x_amt - o_amt) >= 2:
        print('Impossible')
    # Ensure rows and columns don't contain more than 1 winning position
    elif X_WINS in rows and O_WINS in rows:
        print('Impossible')
    elif X_WINS in cols and O_WINS in cols:
        print('Impossible')
    # Define winning logic
    elif game[0] != ' ' and game[0] == game[1] and game[1] == game[2]:
        print(game[0] + ' wins')
        quit()
    elif game[3] != ' ' and game[3] == game[4] and game[4] == game[5]:
        print(game[3] + ' wins')
        quit()
    elif game[6] != ' ' and game[6] == game[7] and game[7] == game[8]:
        print(game[6] + ' wins')
        quit()
    elif game[0] != ' ' and game[0] == game[3] and game[3] == game[6]:
        print(game[0] + ' wins')
        quit()
    elif game[1] != ' ' and game[1] == game[4] and game[4] == game[7]:
        print(game[1] + ' wins')
        quit()
    elif game[2] != ' ' and game[2] == game[5] and game[5] == game[8]:
        print(game[2] + ' wins')
        quit()
    elif game[0] != ' ' and game[0] == game[4] and game[4] == game[8]:
        print(game[0] + ' wins')
        quit()
    elif game[2] != ' ' and game[2] == game[4] and game[4] == game[6]:
        print(game[2] + ' wins')
        quit()
    # Check for game completion
    elif ' ' in game:
        print('Game not finished')
    # Check for draw
    elif ' ' not in game:
        print('Draw')
        quit()


if __name__ == '__main__':
    main()
