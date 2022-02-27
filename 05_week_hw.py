# Rock paper scissors exercise

# User input
rps_input = input("Enter a choice ('r', 'p', 's'): ")

# Using the random method, select either rock paper or scissors
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {rps_input}, computer chose {computer_action}.\n")