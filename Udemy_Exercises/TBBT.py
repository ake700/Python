#A variation of rock, paper, scissors from The Big Bang Theory

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

lizard = '''
                       )/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /          
  `\.-''__.-' \ (     \_      
    `---    `\   /\
                ')
'''
spock = '''                    
                                             88         
                                             88         
                                             88         
,adPPYba, 8b,dPPYba,   ,adPPYba,   ,adPPYba, 88   ,d8   
I8[    "" 88P'    "8a a8"     "8a a8"     "" 88 ,a8"    
 `"Y8ba,  88       d8 8b       d8 8b         8888[      
aa    ]8I 88b,   ,a8" "8a,   ,a8" "8a,   ,aa 88`"Yba,   
`"YbbdP"' 88`YbbdP"'   `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
          88                                            
          88  
'''
'''
'''

import random

game_images = [rock, paper, scissors, lizard, spock]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for lizard, and 4 for Spock.\n"))

if user_choice >= 5 or user_choice < 0:
  print("Invalid number")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 4)
  print("Computer chose:\n" + game_images[computer_choice])

  condition1 = computer_choice == 0 and user_choice == 2
  condition2 = computer_choice == 0 and user_choice == 3
  condition3 = computer_choice == 3 and user_choice == 1
  condition4 = computer_choice == 3 and user_choice == 4
  condition5 = computer_choice == 2 and user_choice == 3
  condition6 = computer_choice == 1 and user_choice == 4
  condition7 = computer_choice == 4 and user_choice == 0
  condition8 = computer_choice == 4 and user_choice == 2

  conditions = [condition1, condition2, condition3, condition4,
             condition5, condition6, condition7, condition8]
    
  if any(conditions):
    print("Lose")
  elif user_choice == computer_choice:
    print("Draw")
  else:
    print("Win")
