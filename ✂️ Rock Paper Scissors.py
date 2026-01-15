#I did this project only with the basis I've learned from my course so far.

import random

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊ Rock")
print("2) ✋ Paper")
print("3) ✌️ Scissors")

user_choice = int(input("Pick a number (1-3): "))
while user_choice < 1 or user_choice > 3:
    user_choice = int(input("Invalid choice. Pick a number (1-3): "))

computer_choice = random.randint(1, 3)

if user_choice == 1 and computer_choice == 1:
    print("You chose ✊ Rock.")
    print("CPU chose ✊ Rock.") 
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
    print("You chose ✊ Rock.")
    print("CPU chose ✋ Paper.") 
    print("The CPU won!")
elif user_choice == 1 and computer_choice == 3:
    print("You chose ✊ Rock.")
    print("CPU chose ✌️ Scissors.") 
    print("The player won!")
elif user_choice == 2 and computer_choice == 1:
    print("You chose ✋ Paper.")
    print("CPU chose ✊ Rock.") 
    print("The player won!")
elif user_choice == 2 and computer_choice == 2:
    print("You chose ✋ Paper.")
    print("CPU chose ✋ Paper.") 
    print("It's a tie!")
elif user_choice == 2 and computer_choice == 3:
    print("You chose ✋ Paper.")
    print("CPU chose ✌️ Scissors.") 
    print("The CPU won!")
elif user_choice == 3 and computer_choice == 1:
    print("You chose ✌️ Scissors.")
    print("CPU chose ✊ Rock.") 
    print("The CPU won!")
elif user_choice == 3 and computer_choice == 2:
    print("You chose ✌️ Scissors.")
    print("CPU chose ✋ Paper.") 
    print("The player won!")
elif user_choice == 3 and computer_choice == 3:
    print("You chose ✌️ Scissors.")
    print("CPU chose ✌️ Scissors.") 
    print("It's a tie!")
    
print("==========================================================================================================")    
print("Okay, you have played Rock, Paper, Scissors, but have you heard of Rock, Paper, Scissors, Lizard, Spock?")
print("It's a fun variation of the classic game brought to popularity with a TV show called The Big Bang Theory.")
print("==========================================================================================================")  
user_choice = input("Would you like to play it? (Yes/No): ")
while user_choice != "Yes" and user_choice != "No":
    user_choice = input("Invalid choice. Would you like to play Rock, Paper, Scissors, Lizard, Spock? (Yes/No): ")
if user_choice == "Yes":
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    print("1) ✊ Rock")
    print("2) ✋ Paper")
    print("3) ✌️ Scissors")
    print("4) 🦎 Lizard")
    print("5) 🖖 Spock")

    user_choice = int(input("Pick a number (1-5): "))

    while user_choice < 1 or user_choice > 5:
        user_choice = int(input("Invalid choice. Pick a number (1-5): "))

    computer_choice = random.randint(1, 5)

    if user_choice == 1 and computer_choice == 1:
        print("You chose ✊ Rock.")
        print("CPU chose ✊ Rock.") 
        print("It's a tie!")
    elif user_choice == 1 and computer_choice == 2:
        print("You chose ✊ Rock.")
        print("CPU chose ✋ Paper.") 
        print("The CPU won!")
    elif user_choice == 1 and computer_choice == 3:
        print("You chose ✊ Rock.")
        print("CPU chose ✌️ Scissors.") 
        print("The player won!")
    elif user_choice == 1 and computer_choice == 4:
        print("You chose ✊ Rock.")
        print("CPU chose 🦎 Lizard.") 
        print("The player won!")
    elif user_choice == 1 and computer_choice == 5:
        print("You chose ✊ Rock.")
        print("CPU chose 🖖 Spock.") 
        print("The CPU won!")
    elif user_choice == 2 and computer_choice == 1:
        print("You chose ✋ Paper.")
        print("CPU chose ✊ Rock.") 
        print("The player won!")
    elif user_choice == 2 and computer_choice == 2: 
        print("You chose ✋ Paper.")
        print("CPU chose ✋ Paper.") 
        print("It's a tie!")
    elif user_choice == 2 and computer_choice == 3: 
        print("You chose ✋ Paper.")
        print("CPU chose ✌️ Scissors.") 
        print("The CPU won!")
    elif user_choice == 2 and computer_choice == 4:
        print("You chose ✋ Paper.")
        print("CPU chose 🦎 Lizard.") 
        print("The CPU won!")   
    elif user_choice == 2 and computer_choice == 5:
        print("You chose ✋ Paper.")
        print("CPU chose 🖖 Spock.") 
        print("The player won!")
    elif user_choice == 3 and computer_choice == 1: 
        print("You chose ✌️ Scissors.")
        print("CPU chose ✊ Rock.") 
        print("The CPU won!")
    elif user_choice == 3 and computer_choice == 2:
        print("You chose ✌️ Scissors.")
        print("CPU chose ✋ Paper.") 
        print("The player won!")
    elif user_choice == 3 and computer_choice == 3: 
        print("You chose ✌️ Scissors.")
        print("CPU chose ✌️ Scissors.") 
        print("It's a tie!")
    elif user_choice == 3 and computer_choice == 4: 
        print("You chose ✌️ Scissors.")
        print("CPU chose 🦎 Lizard.") 
        print("The player won!")
    elif user_choice == 3 and computer_choice == 5: 
        print("You chose ✌️ Scissors.")
        print("CPU chose 🖖 Spock.") 
        print("The CPU won!")
    elif user_choice == 4 and computer_choice == 1: 
        print("You chose 🦎 Lizard.")
        print("CPU chose ✊ Rock.") 
        print("The CPU won!")
    elif user_choice == 4 and computer_choice == 2:
        print("You chose 🦎 Lizard.")
        print("CPU chose ✋ Paper.") 
        print("The player won!")    
    elif user_choice == 4 and computer_choice == 3:
        print("You chose 🦎 Lizard.")
        print("CPU chose ✌️ Scissors.") 
        print("The CPU won!")
    elif user_choice == 4 and computer_choice == 4: 
        print("You chose 🦎 Lizard.")
        print("CPU chose 🦎 Lizard.") 
        print("It's a tie!")
    elif user_choice == 4 and computer_choice == 5: 
        print("You chose 🦎 Lizard.")
        print("CPU chose 🖖 Spock.") 
        print("The player won!")
    elif user_choice == 5 and computer_choice == 1: 
        print("You chose 🖖 Spock.")
        print("CPU chose ✊ Rock.") 
        print("The player won!")
    elif user_choice == 5 and computer_choice == 2:
        print("You chose 🖖 Spock.")
        print("CPU chose ✋ Paper.") 
        print("The CPU won!")
    elif user_choice == 5 and computer_choice == 3: 
        print("You chose 🖖 Spock.")
        print("CPU chose ✌️ Scissors.") 
        print("The player won!")
    elif user_choice == 5 and computer_choice == 4: 
        print("You chose 🖖 Spock.")
        print("CPU chose 🦎 Lizard.") 
        print("The CPU won!")
    elif user_choice == 5 and computer_choice == 5: 
        print("You chose 🖖 Spock.")
        print("CPU chose 🖖 Spock.") 
        print("It's a tie!")
        
else:
    print("Alright, maybe next time!")
