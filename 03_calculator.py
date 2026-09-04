while True:
    operator = input("Enter an operator (+ - * /) or 'q' to quit: ")
    
    if operator == 'q':
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator == "*":
        result = num1 * num2
        print(result)
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print(result)
    else:
        print(f"{operator} is not a valid operator. Pleas try again.")