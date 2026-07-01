import random

## IMPORTANT:# These ASCII art are from { wynand1004 / RPS_ASCII_Art.py }

# 0 for rock, 1 for paper, 2 for scissors

ascii_rock = r'''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
ascii_paper = r'''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
ascii_scissor = r'''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''



ascii_art = [ascii_rock, ascii_paper, ascii_scissor]


random_computer_decision = random.randint(0, 2)


computer_virtual_hand = ""

if random_computer_decision == 0:
    computer_virtual_hand = "rock"
    
elif random_computer_decision == 1:
    computer_virtual_hand = "paper"  
    
else:
    computer_virtual_hand = "scissor"

user_decision = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissor: "))
user_hand = ""

if user_decision == 0:
    user_hand = "rock"
elif user_decision == 1:
    user_hand = "paper"
else:
    user_hand = "scissor"

print("You:")
print(ascii_art[user_decision])
print("\n\n Computer:")
print(ascii_art[random_computer_decision])

# Deciding the winner

if (user_hand == "rock" and computer_virtual_hand == "scissor") or (user_hand == "paper" and computer_virtual_hand == "rock") or (user_hand == "scissor" and computer_virtual_hand == "paper"):
    print("\nYou won")
elif (computer_virtual_hand == "rock" and user_hand == "scissor") or (computer_virtual_hand == "paper" and user_hand == "rock") or (computer_virtual_hand == "scissor" and user_hand == "paper"):
    print("\nYou lose")
elif computer_virtual_hand == user_hand:
    print("\nDraw")



    
    
