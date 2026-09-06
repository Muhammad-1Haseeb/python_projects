menu = {
    "popcorn": 5,
    "soda": 3,
    "candy": 2,
    "water": 1,
    "nachos": 4,
    "hotdog": 3
}

cart = []

total = 0

print("------------ Menu ------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------------------")

while True:
    food = input("Enter the food item you want to add to your cart (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------ Your Order ------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")