import random 

computer_guess = (random.randint(1, 100))

guess_answer = 0
attempts = 0

def game_difficulty():    

    difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ")
    if difficulty == 'easy':
        play_game(10)
        
    else:
        play_game(5)       
    

def play_game(attempts):
    
    global guess_answer
    global computer_guess

    while attempts > 0:
        guess()
        if guess_answer > computer_guess:
            attempts -= 1
            print("Too high")
            print (f"You have {attempts} attempts remaining to guess the number.")

        elif guess_answer < computer_guess:
            attempts -= 1
            print("Too low")
            print (f"You have {attempts} attempts remaining to guess the number.")

        elif guess_answer == computer_guess:
            print("Congrats you guessed right!")
            break
        
        elif attempts == 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            print("Game over, the correct number was {computer_guess}")


def guess():
    global guess_answer
    guess_answer = int(input("Make a guess: "))
    return guess_answer

game_difficulty()