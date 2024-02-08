#add
def add (n1, n2):
    return n1+n2

#substract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply (n1, n2):
    return n1*n2

#divide
def divide (n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

end_of_calculation = False

num1 = float(input("What's the first number?: "))
num2 = float(input("What's the second number?: "))

for symbols in operations:
    print (symbols)


while not end_of_calculation:   
    operation_symbol = input("Pick an operation: ")    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    rounded_answer = round(answer, 4)
    print (f'{num1} {operation_symbol} {num2} = {rounded_answer}')
    continue_calculation = (input(f"Type 'y' to continue calculating with {rounded_answer}, or type 'n' to start a new calculation: "))
    num1 = answer 

    if continue_calculation == "y":
        next_number = float(input("What's the next number?: "))
        num2 = next_number
    if continue_calculation == "n":
        end_of_calculation = True
        