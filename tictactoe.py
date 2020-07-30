def boardgame(status):
    column = 3
    row = 3
    # Print the current game
    print('-' * 9)
    for i in range(row):
        print('|', end=' ')
        for j in range(column):
            print(status[j + (column * i)], end=' ')
        print('|')
    print('-' * 9)

def how_to_win(status):
    # What it needs to win
    x_win = ['X', 'X', 'X']
    o_win = ['O', 'O', 'O']

    # List of rows to check
    winning_rows = [status[:3], status[3:6], status[6:9], status[0::3], status[1::3], status[2::3],
                    [status[0]] + [status[4]] + [status[8]],
                    [status[2]] + [status[4]] + [status[6]]]

    # Check the amount of winning row(s)
    x_flag = 0
    o_flag = 0
    if x_win in winning_rows: x_flag += 1
    if o_win in winning_rows: o_flag += 1

    message = ""
    winner = False

    # Feedback to user(s)
    if x_flag > 0 and o_flag > 0:
        message = "Impossible"
    elif abs(status.count('X') - status.count('O')) > 1:
        message = "Impossible"
    elif status.count(' ') == 0 and x_flag == 0 and o_flag == 0:
        message = "Draw"
        winner = True
    elif x_flag == 0 and o_flag == 0 and status.count('_') > 0:
        message = "Game not finished"
    elif x_flag == 1:
        message = "X wins"
        winner = True
    elif o_flag == 1:
        message = "O wins"
        winner = True

    return message, winner

def user_move(status):
    position_dict = {0: [1, 3], 1: [2, 3], 2: [3, 3], 3: [1, 2], 4: [2, 2], 5: [3, 2], 6: [1, 1], 7: [2, 1], 8: [3, 1]}
    val_position = list(position_dict.values())
    player_turn = "X"

    while True:
        user_move = input("Enter the coordinates: ").split()
        if not user_move[0].isdecimal() or not user_move[1].isdecimal():
            print("You should enter numbers!")
            continue

        user_move[0] = int(user_move[0])
        user_move[1] = int(user_move[1])

        if user_move[0] > 3 or user_move[1] > 3:
            print("Coordinates should be from 1 to 3!")
        elif status[(val_position.index(user_move))] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            status[val_position.index(user_move)] = player_turn
            boardgame(status)
            print(how_to_win(status)[0])
            if how_to_win(status)[1]:
                break
            else:
                if player_turn == "X":
                    player_turn = "O"
                else:
                    player_turn = "X"


if __name__ == "__main__":
    status = "         "
    boardgame(list(status))
    user_move(list(status))
