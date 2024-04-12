# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instruction():
    print('''


**** Instructions ****

- Users can optionally read the instructions before starting to play.

- Users can either choose the number of rounds or they can opt for infinite mode.

- Users choose the parameters for the game (ie: they choose the range involved which means they need to give us a low number and a high number where the mystery number will be between the two numbers we are given at the start of the game).

- If users press the exit code ‘xxx’ or play the requested number of rounds, then the game should end.

- When the game ends, users should be able to choose to see their game history.

    ''')


# Main routine
print()
print("Welcome to the Higher Lower Game")
print()
# loop for testing


want_instructions = yes_no("Do you want to read the instructions?").lower()
# checks user enter y or n
if want_instructions == "yes":
    instruction()
print("program continues")
