# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
print(f"Computer chose {computer_choice}")

# Run Conditionals
if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "r":
    if computer_choice == "s":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "p":
    if computer_choice == "r":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "s":
    if computer_choice == "p":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

else:
    print("I don't understand that, next time choose 'r', 'p' or 's'")




