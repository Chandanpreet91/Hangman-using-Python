from hangman_images import stages, logo
from hangman_words import word_list
import random
print(logo) 
random_word = random.choice(word_list) 
lives = 6
print(f'You random word is {random_word}')
display = []
for word in random_word:
    display += "_"
end_of_game = False
print(display)
while not end_of_game:
    guess = input("Please Guess a letter ")
    for position in range(len(random_word)):
        word = random_word[position]
        if word == guess:
            display[position] = word
            
    if guess not in random_word:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                end_of_game = True
                print('You Lose')
        
    print(display)    
if "_" not in display:
        print("You win")
        end_of_game = True
    
       
