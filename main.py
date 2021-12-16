import random
# to create a function, do 
# def function():
# funcions can be nested

# Pick the word
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# generate the list
letters_list = []
for spot in range(len(chosen_word)):
  letters_list.append('_')

print(chosen_word)
print(letters_list)

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter ").lower()
  # Iterate through word to check for letter and replace in word list where appropriate
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    
    if letter == guess:
      letters_list[position] = letter
      print("right")
    else:
      print ("wrong")
    print(letters_list)
  # check if player has won by seeing if there are still any "_" left in letters_list
  if "_" not in letters_list:
    end_of_game = True
    print("You win!")