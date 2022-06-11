from replit import clear 
import random
from Hangman_words import word_list 

random_num = random.randint(0, 2)
if random_num == 0:
  chosen_word = random.choice(word_list[0])
elif random_num == 1:
  chosen_word = random.choice(word_list[1])
elif random_num == 2:
  chosen_word = random.choice(word_list[2])

stages = [0, 1, 2, 3, 4, 5]
end_of_game = False 
display = []
word_length = len(chosen_word)
lives = 6

for letter in range(word_length):
  display += "_"
print(display)

while not end_of_game:  
  if random_num == 0:
    print(f"Hint: your topic is bacterial genera")
  elif random_num == 1:
    print(f"Hint: your topic is fruit")
  elif random_num == 2:
    print(f"Hint: your topic is major city")
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in display:
    print(f"You've already guessed {guess}")
  for letter_position in range(word_length):
    letter = chosen_word[letter_position]
    if letter == guess:
      display[letter_position] = letter
    #Can't print no match here b/c it loops through the guesses
  print(display)
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose")
  if "_" not in display: #if blank in list is no longer true:
    end_of_game = True
    print("You win")
  print(f"You have {stages[lives]} lives remaining.")
  if end_of_game == True:
    print(f"The word is {chosen_word}")
