def tic_tac_toe():
    print()
    print('-------------')
    print("Tic Tac Toe")
    print('-------------')

    def game():
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        def print_board():
            print()
            print(board[0] + " | " + board[1] + " | " + board[2])
            print(board[3] + " | " + board[4] + " | " + board[5])
            print(board[6] + " | " + board[7] + " | " + board[8])

        def winnerCheck(player):
            w_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (3, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
            return any(board[a] == board[b] == board[c] == player for a, b, c in w_combos)

        turn = "X"
        for _ in range(9):
            print_board()
            while True:
                try:
                    move = (int(input("pick a spot, 1-9: ")) - 1)
                    if move > 8 or move < 0:
                        print("Enter 1-9")
                    elif board[move] in ['X', 'O']:
                        print("Spot already taken")
                    else:
                        break
                except ValueError:
                    print("Type a number")

            board[move] = turn
            if winnerCheck(turn):
                print_board()
                print(f"Player {turn} wins")
                break
            turn = "O" if turn == "X" else "X"
        else:
            print_board()
            print("It's a tie")
    game()
