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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_choice = ""

if choice == 0 :
    print(rock)
    user_choice = rock
elif choice == 1:
    print(paper)
    user_choice = paper
elif choice == 2:
    print(scissors)
    user_choice = scissors
else:
    print("Wrong input. Type 0 for Rock, 1 for Paper or 2 for Scissors.")

random_number = random.randint(0, 2)
computer_choice = ""

print("Computer's Chose: \n")

if random_number == 0:
    print(rock)
    computer_choice = rock
elif random_number == 1:
    print(paper)
    computer_choice = paper
elif random_number == 2:
    print(scissors)
    computer_choice = scissors

if user_choice == rock:
    if computer_choice == paper:
        print("You lose")
    elif computer_choice == rock:
        print("Draw")
    else:
        print("You Win!!")
elif user_choice == paper:
    if computer_choice == rock :
        print("You Win!!")
    elif computer_choice == paper:
        print("Draw")
    elif computer_choice == scissors:
        print("You lose")

else:
    if computer_choice == rock:
        print("You lose")
    elif computer_choice == paper:
        print("You Win!!")
    else:
        print("Draw")