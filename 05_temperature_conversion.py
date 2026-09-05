unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 *temp ) / 5+ 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} F")
elif unit == "F":
    temp = round((5 * (temp - 32)) / 9, 1)
    print(f"The temperature in Celsius is: {temp} C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

print(f"Temperature: {temp} {unit}")