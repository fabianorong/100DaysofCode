print("Welcome to the secret auction program.")

end_of_bidders = False
bidders = {}
highest_bid = 0
i = 0
winner_name = 0

while not end_of_bidders:
    name = input("What is your name?: ")    
    bid = int(input("What's your bid?: "))
    bidders[name] = bid    

    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bid = bidders[key]
            winner_name = key

    if any_other_bidders == "no":
        end_of_bidders = True
print (f'The winner is {winner_name} with a bid of ${highest_bid}')        
