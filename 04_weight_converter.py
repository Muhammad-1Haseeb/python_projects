# Weight converter 

weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds (K or P): ")

if unit.upper() == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit.upper() == "P":
    weight = weight / 2.205
    unit = "Kg."
else:
    print(f"{unit} is not a valid unit. Please try again.")

print(f"Weight: {round(weight, 1)} {unit}")
