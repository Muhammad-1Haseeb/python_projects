# Compound Interest Calculator

principal = 0
rate = 0
time = 0

while principal <=0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than 0. Please try again.")

while rate <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")

while time <=0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")

total = principal * pow((1 + rate / 100), time)

print(f"The total amount after {time} years is: {total: .2f}")