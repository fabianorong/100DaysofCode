from game_data import data
import random

def get_random_celeb():
    random_celeb = random.choice(data)
    return (random_celeb)
    
def celeb_description(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    
    return f"{name}, {description}, {country}"

def answer_method():
    answer = input("Who has more followers? Type 'A' or 'B': ")
    answer = answer.lower()
    return answer


def celeb_followers_number(account):
    followers_number = account["follower_count"]
    return followers_number

def game_repeat():
    game_repeat_answer = input("Do you want to play again? 'Y' or 'N'")
    game_repeat_answer = game_repeat_answer.lower()
    return game_repeat_answer

def game():
    score = 0
    game_on = True

    acc1 = get_random_celeb()    

    while game_on:
        acc1_number_followers = celeb_followers_number(acc1)
        acc1_desc = celeb_description(acc1)

        acc2 = get_random_celeb()
        while acc2 == acc1:
            acc2 = get_random_celeb()
        acc2_number_followers = celeb_followers_number(acc2)
        acc2_desc = celeb_description(acc2)

        print (f"Compare A: {acc1_desc}\n")
        print("VS\n")
        print (f"Against B: {acc2_desc}\n")
        answer = answer_method()

        if answer == 'a' and acc1_number_followers > acc2_number_followers:
            score += 1
            print(f"You're right! Current score: {score}\n")
            acc1 = acc2
        if answer == 'b' and acc1_number_followers < acc2_number_followers:
            score += 1
            print(f"You're right! Current score: {score}\n")
            acc1 = acc2
        if answer == 'a' and acc1_number_followers < acc2_number_followers:
            print(f"Sorry, that's wrong.\nYour final score: {score}\n")
            game_repeat_ans = game_repeat()
            if game_repeat_ans == 'y':
                game()
            else:
                game_on = False
        if answer == 'b' and acc1_number_followers > acc2_number_followers:
            print(f"Sorry, that's wrong.\nFinal score: {score}\n")
            game_repeat_ans = game_repeat()
            if game_repeat_ans == 'y':
                game()
            else:
                game_on = False
game()

        
            


        


    
  

