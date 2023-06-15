import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gameimgs = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"))
print(f'You chose: {user_choice}')

if user_choice >= 3 or user_choice < 0:
    print("You chose an invalid number. You lose!")
else:
    print(gameimgs[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(gameimgs[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw!")
