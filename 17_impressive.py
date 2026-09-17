import math

for y in range(15, -15, -1):
    for x in range(-30, 30):
        X = x / 15
        Y = y / 10
        f = (X**2 + Y**2 - 1)**3 - X**2 * Y**3  # Fixed operator here
        print("*" if f <= 0 else " ", end=" ")
    print()