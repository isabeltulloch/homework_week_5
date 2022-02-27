import random
# !!import random module to use random.randit

# name variables
comp_wins = 0
player_wins = 0

# function to call options
def Choose_Option():
    player_choice = input("Choose Rock (R), Paper (P) or Scissors (S): ")
    if player_choice in ["Rock", "rock", "r", "R"]:
        # user can type in any of the above
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "s"
        # if and elif statements defining player inputs
    else:
        # if user doesn't correctly select out of selections then message will appear
        print("Invalid input, please try again.")
        # message will show if user input does not match any of the above
        Choose_Option()
    return player_choice
# return defines the function, above function will return the players choice, depending on user input


# now to define computers actiona/options
def Computer_Option():
    comp_choice = random.randint(1, 3)
    # random integer selection between 1 and 3, 1, 2, 3
    if comp_choice == 1:
        # define what each number will represent
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        # always finish with else statement!!
        comp_choice = "s"
    return comp_choice


# loop statement to allow game to flow
while True:
    print("")
    # not sure why these were added, ask
    # apparently for spaces?

    player_choice = Choose_Option()
    comp_choice = Computer_Option()

    # defining functions as varaibles - easy to call now

    print("")

    if player_choice == "r":
        if comp_choice == "r":
            print("Player1: Rock\nComputer: Rock\n ...You tied.")

        elif comp_choice == "p":
            print("Player1: Rock\nComputer: Paper\n ...You lose.")
            comp_wins += 1

        elif comp_choice == "s":
            print("Player1: Rock\nComputer: Scissors\n ...You win!")
            player_wins += 1
# write down all possible outcomes for choices, should have 9 choices, double check
    elif player_choice == "p":
        if comp_choice == "r":
            print("Player1: Paper\nComputer: Rock\n ...You win!")
            player_wins += 1

        elif comp_choice == "p":
            print("Player1: Paper\nComputer: Paper\n ...You tied.")


        elif comp_choice == "s":
            print("Player1: Paper\nComputer: Scissors\n ...You lose.")
            comp_wins += 1
# splitting options to make it more visible in regards to code, showing each option and logic
    elif player_choice == "s":
        if comp_choice == "r":
            print("Player1: Scissors\nComputer: Rock\n ...You lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("Player1: Scissors\nComputer: Paper\n ...You win!")
            player_wins += 1

        elif comp_choice == "s":
            print("Player1: Scissors\nComputer: Scissors\n ...You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    # add values of scores, calcalution to add scores
    print("Computer wins: " + str(comp_wins))
    # not sure why it was converted to a string also, ask why
    print("")

    player_choice = input("Do you want to play again? (yes/no)")
    if player_choice in ["Y", "y", "yes", "Yes"]:
        continue
    # pass = continue, continue = pass, learned about continue used that instead
    elif player_choice in ["N", "n", "no", "No"]:
        break
        # break, stops
    else:
        break