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
# print(rock)
# print(paper)
# print(scissors)
import random
items=[rock, paper, scissors]
choice=int(input("What item do you choose? . "
                 "Type 0 for rock, 1 for paper and 2 for scissors \n"))
print(f"You chose: {items[choice]}")
if choice < 0 or choice > 2:
    print("Wrong input, game over")
if choice ==0:
    print(rock)
elif choice ==1:
    print(paper)
elif choice==2:
    print(scissors)
else:
    print("Wrong input, game over")
computer_choice=int(random.randint(0,2))
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)

if computer_choice==choice:
    print("Draw")
elif computer_choice==0 and choice==1:
    print("You win")
elif computer_choice==0 and choice==2:
    print("Computer wins")

elif choice==0 and computer_choice==1:
    print("Computer wins")
elif choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==1 and choice==0:
    print("Computer wins")
elif computer_choice==1 and choice==2:
    print("You win")
elif choice==1 and computer_choice==0:
    print("You win")
elif choice==1 and computer_choice==2:
    print("Computer wins")
elif computer_choice==2 and choice==0:
    print("You win")
elif computer_choice==2 and choice==1:
    print("Computer wins")
elif choice==2 and computer_choice==0:
    print("Computer wins")
elif choice==2 and computer_choice==1:
    print("You win")
else:
    print("Wrong code, Computer wins."
          "Game over")

