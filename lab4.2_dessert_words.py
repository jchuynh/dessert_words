##LAB 4.2: Dessert Words 

#discarded code
##comment

##using VS Code and Git bash terminal within program.'
##to run code ctrl+alt+n
##to stop code run ctrl+alt+mb
##to choose language to run ctrl+alt+j --> then select language



import random

dessert_words = ["pie", "pudding", "cake", "cookies", "doughnut", "baklava", "cheesecake", "sundae", "candy"]

secret_word = random.choice(dessert_words)
#secret_word = "pudding"
print(secret_word)
secret_word_length = len(secret_word)
print(secret_word_length)

print("Guess the dessert!")
user_guess = input("Guess a letter! > ")

def handle_guess(user_guess, letters_guessed, secret_word):
    """handling user letter guess."""
    ##pseudocode:
    ##input letter guess.
    ##test in while loop
    ##letter is tested against secret word
    ##if letters do not appear in secret word, place letter in dictionary and reply to user that it is incorrect
    ##if letter appears in secret word , reply correct and print out letter (letter should still be palce in dictionary as a guess)
    ##complete when all the leters have been guess in the corect order


##inital fuction written to handle the secret word
#def guess_word(word):
  #while True:
  #letters_guess = {}
  #for letter in secret_word:
    #if user_guess == secret_word[letter]:
      #print("That's correct!")
      #print(secret_word[letter])
    #else:
      #print("Try again")
      #print("Letters Guessed: {}".format(letters_guessed)
  #elif user_guess = secret

#guess_word(secret_word)

  