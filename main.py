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


import random
images=[rock,paper,scissors]
print("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.")
user=int(input())
print(images[user])
print("computer choose:")
computer=random.randint(0,2)
print(images[computer])
if computer==2 and user==0:
  print("You Win!")
elif user==2 and computer==0:
  print("You Lose!")
elif user > computer:
  print("you win!")
elif computer > user:
  print("You lose!")
elif computer==user:
  print("It's a draw")