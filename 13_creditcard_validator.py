# 1. Remove any '-' or ' '
# 2. Add all the digits in the odd places from right to left
# 3. Double every second digit from right to left, (if result is a two digit number together to get a single digit.)
# 4. Sum the total of step 2 and step 3
# 5. If the total is divisible by 10, then the number is valid,

sum_odd_digits = 0
sum_even_digits = 0
total = 0


# Step 1
card_number = input("Enter the credit card number: ")
card_number = card_number.replace("-", "").replace(" ", "")
card_number = card_number[::-1]

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")