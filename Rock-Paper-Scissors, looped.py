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

while True:
    import random
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        print("Invalid choice")
        
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)
    else:
        print("Invalid choice")

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win")
    elif user_choice == computer_choice:
        print("Draw")
    else:
        print("You lose")
