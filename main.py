import random
# to create a function, do 
# def function():
# funcions can be nested

# Hangman images
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
lives = 6
# Pick the word
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# generate the list
letters_list = []
for spot in range(len(chosen_word)):
  letters_list.append('_')
# Cheat
print(chosen_word)
print(letters_list)

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter ").lower()
  correct_checks = 0
  # Iterate through chosen word to check for letter and replace in word list where appropriate
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      letters_list[position] = letter
      correct_checks += 1
  # If after the word has been checked there are no matches, lose a life
  if correct_checks < 1:
    lives -= 1
  # display art and current letters
  print(stages[lives])
  print(f"{' '.join(letters_list)}")
  # check if player has lost by losing too many lives
  if lives < 1:
    end_of_game = True
    print("You lost!")
  # check if player has won by seeing if there are still any "_" left in letters_list
  if "_" not in letters_list:
    end_of_game = True
    print("You won!")
  