MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def drink_choice():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice.lower() in ['report', 'espresso', 'latte', 'cappuccino']:
            return choice.lower()
        else:
            print("Invalid choice. Please select from espresso, latte or cappuccino")
    

def insert_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    quarters = quarters * 0.25

    dimes = float(input("How many dimes?: "))
    dimes = dimes * 0.10

    nickels = float(input("How many nickels?: "))
    nickels = nickels * 0.05

    pennies = float(input("How many pennies?: "))
    pennies = pennies * 0.01

    total = quarters + dimes + nickels + pennies
    return total

def change(total_input, drink_cost):
    total_change = total_input - drink_cost
    total_change = round(total_change, 3)

    return f"Here is ${total_change} in change."

def cost(drink):
    drink_choice = MENU[drink]
    drink_choice_cost = drink_choice["cost"]
    return drink_choice_cost

def water_ingredients(drink):
    drink_choice =  MENU[drink]
    drink_ingredients = drink_choice["ingredients"]
    water = drink_ingredients["water"]    
    return water

def milk_ingredients(drink):
    drink_choice =  MENU[drink]
    drink_ingredients = drink_choice["ingredients"]    
    milk = drink_ingredients["milk"]    
    return  milk

def coffee_ingredients(drink):
    drink_choice =  MENU[drink]
    drink_ingredients = drink_choice["ingredients"]    
    coffee = drink_ingredients["coffee"]
    return coffee

def tank():
    tank_water = resources["water"]
    tank_milk = resources["milk"]
    tank_coffee = resources["coffee"]
    return tank_water, tank_milk, tank_coffee

def coffe_machine():
    machine_on = True
    tank_water, tank_milk, tank_coffee = tank()
    money = 0

    while machine_on:
        drink_choice_text = drink_choice()
        

        if drink_choice_text == 'report':
            print(f"Water: {tank_water}ml")
            print(f"Milk: {tank_milk}ml")
            print(f"Coffee: {tank_coffee}g")
            print(f"Money: ${money}")          
        
            
        if drink_choice_text == "espresso":

            drink_price = cost(drink_choice_text)
            water = water_ingredients(drink_choice_text)
            coffee = coffee_ingredients(drink_choice_text)

            if (tank_water > water) and (tank_coffee > coffee):                    
                tank_coffee = tank_coffee - coffee
                tank_water = tank_water - water
                total_input_money = insert_coins()
                if total_input_money > drink_price:
                    change_text_value = change(total_input_money, drink_price)
                    print(change_text_value) 
                    money = money + drink_price
                    print(f"Here is your {drink_choice_text} Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")

            if (tank_water < water):
                    print("Sorry there is not enough water.")
            elif (tank_coffee < coffee):
                    print("Sorry there is not enough coffee.")
            
            
        if drink_choice_text == "latte":

            drink_price = cost(drink_choice_text)
            water = water_ingredients(drink_choice_text)
            coffee = coffee_ingredients(drink_choice_text)
            milk = milk_ingredients(drink_choice_text)

            if (tank_water < water):
                print("Sorry there is not enough water.")
            elif (tank_coffee < coffee):
                print("Sorry there is not enough coffee.")
            elif (tank_milk < milk):
                print("Sorry there is not enough milk.")        

            if (tank_water > water) and (tank_coffee > coffee) and (tank_milk > milk):
                tank_coffee = tank_coffee - coffee
                tank_water = tank_water - water
                tank_milk = tank_milk - milk
                total_input_money = insert_coins()
                if total_input_money > drink_price:
                    change_text_value = change(total_input_money, drink_price)
                    print(change_text_value) 
                    money = money + drink_price
                    print(f"Here is your {drink_choice_text} Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            

        if drink_choice_text == "cappuccino":
            
            drink_price = cost(drink_choice_text)
            water = water_ingredients(drink_choice_text)
            coffee = coffee_ingredients(drink_choice_text)
            milk = milk_ingredients(drink_choice_text)   

            if (tank_water < water):
                print("Sorry there is not enough water.")
            elif (tank_coffee < coffee):
                print("Sorry there is not enough coffee.")
            elif (tank_milk < milk):
                print("Sorry there is not enough milk.") 

            if (tank_water > water) and (tank_coffee > coffee) and (tank_milk > milk):
                tank_coffee = tank_coffee - coffee
                tank_water = tank_water - water
                tank_milk = tank_milk - milk
                total_input_money = insert_coins()
                if total_input_money > drink_price:
                    change_text_value = change(total_input_money, drink_price)
                    print(change_text_value) 
                    money = money + drink_price
                    print(f"Here is your {drink_choice_text} Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")         
                                 
coffe_machine()