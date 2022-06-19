import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
empty_list = []
end_of_game = False
lives = 6

print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
  letter = "_"
  empty_list.append(letter)

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  iteration = 0
  
  for letter in chosen_word:
    iteration += 1
    
    if letter == guess:
      empty_list[iteration - 1] = letter

  if guess not in chosen_word:
    lives -= 1
      
  print(f"{' '.join(empty_list)}\n", stages[lives])

  if "_" not in empty_list:
    end_of_game = True
    print("You Won!")
  elif lives <= 0:
    end_of_game = True
    print("You Lose!")

