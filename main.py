from tictactoe import tic_tac_toe
from guessthenumber import guess_the_number
from guesstheword import guess_the_word



def GameHub():
    print('---------------------------------------')
    print("Terminal Games!!!")
    print('---------------------------------------')

    print()
    print('<1> Guess the number.')
    print('<2> Guess the word.')
    print('<3> Tic Tac Toe (2 players)')
    print('<99> To Exit')
    print('---------------------------------------')
    while True:
        try:
            select_game = int(input('What game do you want to play: '))

            if select_game == 1:
                guess_the_number()
                GameHub()
            elif select_game == 2:
                guess_the_word()
                GameHub()
            elif select_game == 3:
                tic_tac_toe()
                GameHub()
            elif select_game == 99:
                quit_game = input("Are you sure you want to quit? Y/N: ").lower()
                if quit_game == 'y':
                    break
                elif quit_game == 'n':
                    GameHub()
                    print()
                else:
                    print('Type Y or N')


            else:
                print("Select from 1 - 3 games or 99 to Exit.")

        except ValueError:
            print("Type a number")


GameHub()
