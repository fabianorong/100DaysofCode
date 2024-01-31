print("welcome to the tip calculator.")
total_bill = (input("What was the total bill?\n"))

percentage_tip = (input("What percentage tip would you like to tip? 10, 12 or 15?\n"))

people_qnty = (input("How many people to split the bill?\n"))

tip = (((float(percentage_tip))*0.01) + 1)

each = (float(total_bill)*(float(tip))) /(int(people_qnty))

print(f"Each person should pay: {each}")