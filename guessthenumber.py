def guess_the_number():

    print()
    print('---------------------------------------')
    print("Guess the Number")
    print("I'm thinking of a number from 1 - 100")
    print('---------------------------------------')
    import random

    def game():
        no_to_be_guessed = random.randint(1, 100)
        attempts = 1
        while True:
            try:
                guessed_no = int(input("Your guess? : "))
                if guessed_no > 100 or guessed_no < 0:
                    print("Enter a number, 1 - 100")
                elif guessed_no > no_to_be_guessed:
                    attempts += 1
                    print("Your number is higher")
                elif guessed_no < no_to_be_guessed:
                    attempts += 1
                    print("Your number is lower")
                else:
                    print(f"You guessed right in {attempts} attempt(s)")
                    print()
                    break
            except ValueError:
                print("Type a number")

    game()
