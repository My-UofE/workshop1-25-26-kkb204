import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val:
        if user_input == "h":
            return True
        else:
            return False
    if next_val < current_val:
        if user_input == "l":
            return True
        else:
            return False 

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter not in word:
        print(f"Sorry, '{letter}' is not in the word")
        return False
    else:
        word_list = []
        index_list = []
        for character in word:
            word_list.append(character)
        for item in word:
            if letter in word:
                letter_index = word_list.index(letter)
                index_list.append(letter_index)
        for index in index_list:
            board[index] = letter
        print(f"Well done! '{letter}' is in the word")
        return True

