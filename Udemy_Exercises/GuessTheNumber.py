from random import randint
from replit import clear

EASY_TURNS = 10
HARD_TURNS = 5

def difficult():
  level = input("Choose a difficulty 'easy' or 'hard': ")
  if level == "easy":
    return EASY_TURNS
  elif level == "hard":
    return HARD_TURNS
  else:
    print("Invalid level")
    level = input("Choose a difficulty 'easy' or 'hard': ")
    
def check(guess, number, turns):
  if guess > number:
    print("Too high.")
    return turns - 1
  elif guess < number:
    print("Too low.")
    return turns - 1
  else:
    print(f"You're correct. The answer is {number}")
    
def game():
  print("I'm thinking of a number between 100 and 200")
  number = randint(100, 200)
  turns = difficult()
  guess = 0 
  while guess != number: 
    print(f"You have {turns} attempts remaining.")
    guess = int(input("My guess is: "))
    turns = check(guess, number, turns)
    if turns == 0:
      print("You are out of turns. You lose")
      return 
    elif guess != number:
      print("Try again")
  
while input("Do you want to play the Number Guessing Game? Type 'y' or 'n'\n") == "y":
  clear()
  game()
