# word guessing game
import random

# create a list of words that the user can guess
words_list = ["python","java","ruby","php","rails","rust"]

# select a random word
selected_word = random.choice(words_list)

# initialise game variables
attempts = 4

# set guessed letters to an empty array
guessed_letters = []

# main game loop
while attempts > 0:
    # dis[play word with hidden letters
    display_word = ""
    for letter in selected_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
            
    print(f"word: {display_word}")
    
    # take player input
    guess = input("guess a letter? ").lower()
    
    # check if letter is in the guessed letter array meaning it has already been guessed
    if guess in guessed_letters:
        print("that letter has already been guessed correctly!")
        
        continue
    
    # check if the guess exists in the selected word by random.choic() module
    if guess in selected_word:
        print("guess is correct!")
        # add guessed letter to list of correct guesses
        # this helps in displaying the correct letter guessed or dash
        guessed_letters.append(guess)
    else:
        if attempts == 2:
            print(f"incorrect guessed letter.you have {attempts} attempts left. one more and its game over.")
        else:
             print(f"incorrect guessed letter.you have {attempts} attempts left.")
        attempts -= 1
        
    # check if word has been completely guessed
    if all(letter in guessed_letters for letter in selected_word):
        print(f"you guessed the correct word: {selected_word}")
        
        # end the loop
        break
    
    # end game
    if attempts == 0:
        print(f"game over you lost. out of attempst. the correct word was: {selected_word}")