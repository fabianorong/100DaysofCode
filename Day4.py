import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computerchoice = random.randint(0,2)

if choice == "0":
    print(rock)
    print("Computer chose:\n")
    if computerchoice == 0:
        print(rock)
        print("It's a draw")
    elif computerchoice == 1:
        print(paper)
        print("You lose")
    elif computerchoice == 2:
        print(scissors)
        print("You win")

if choice == "1":
    print(paper)
    print("Computer chose:\n")
    if computerchoice == 0:
        print(rock)
        print("You win")
    elif computerchoice == 1:
        print(paper)
        print("It's a draw")
    elif computerchoice == 2:
        print(scissors)
        print("You lose")

if choice == "2":
    print(scissors)
    print("Computer chose:\n")
    if computerchoice == 0:
        print(rock)
        print("You lose")
    elif computerchoice == 1:
        print(paper)
        print("You win")
    elif computerchoice == 2:
        print(scissors)
        print("It's a draw")
    