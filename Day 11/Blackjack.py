import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
computer_card = []
computer_first_card = 0
current_score = 0
computer_final_score = 0
end_of_game = False

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if want_to_play == "y":
    first_two_cards = random.sample(cards, 2)
    my_cards.append(first_two_cards)
    current_score = sum(my_cards[0])
    computer_first_card = (random.choice(cards))
    computer_card.append(computer_first_card)

    print(f'Your cards: {my_cards[0]}, current score: {current_score}')
    print(f"Computer's first card: {computer_first_card}")   
     
while not end_of_game:
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
    if get_another_card == "y":

        my_cards[0].append(random.choice(cards))
        print(f'Your cards: {my_cards[0]}, current score: {sum(my_cards[0])}')
        print(f"Computer's first card: {computer_card[0]}")

    if get_another_card == 'n':

        while (sum(computer_card)) < (sum(my_cards[0])) and (sum(computer_card)) < 21:
            computer_card.append(random.choice(cards))
            
            if (sum(computer_card)) < 21 and ((sum(computer_card)) > (sum(my_cards[0]))) :
                computer_final_score = (sum(computer_card))
                end_of_game = True

            if (sum(computer_card)) > 21:
                del computer_card[-1]
                
                end_of_game = True

            if (sum(my_cards[0])) > 21 and (sum(computer_card)) < 21:
                end_of_game = True


        print(f'Your final hand: {my_cards[0]}, final score: {sum(my_cards[0])}')
        print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)} ")


        
                      
                

# Your cards: [8, 8], current score: 16
# Computer's first card: 10
# Type 'y' to get another card, type 'n' to pass:
# Your final hand: [9, 7, 3], final score: 19
# Computer's final hand: [6, 2, 3, 7], final score: 18