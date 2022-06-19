from replit import clear
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
empty_list = []
end_of_game = False
lives = 6

print(hangman_art.logo)
print(f"Pssst, the solution is {chosen_word}.")

for letter in chosen_word:
  letter = "_"
  empty_list.append(letter)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  clear()

  if guess in empty_list:
    print(f"You've already guessed '{guess}'.")
  
  iteration = 0
  
  for letter in chosen_word:
    iteration += 1
    
    if letter == guess:
      empty_list[iteration - 1] = letter

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
      
  print(f"{' '.join(empty_list)}\n", hangman_art.stages[lives])

  if "_" not in empty_list:
    end_of_game = True
    print("You Won!")
  elif lives <= 0:
    end_of_game = True
    print("You Lose!")

