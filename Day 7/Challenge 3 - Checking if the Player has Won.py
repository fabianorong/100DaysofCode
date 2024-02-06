import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display =[]
i = 0
game_won = False

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
    while len(display) < len(chosen_word):
        display.append("_")     

end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:    
        if letter == guess:
            display[i] = guess
            i += 1            
        else:
            i += 1        
    print(display)

    if '_' not in display:
        end_of_game = True
        print("You win")               
