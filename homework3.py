
try:
    weight = float(input("Weight in kg: "))
except ValueError:
    print("Please enter a valid weight")
    quit()
        
if weight <= 0:
    print("Please enter a valid weight")
    quit()
elif weight <= 1:
    price = 40
elif weight <= 5:
    price = 80
elif weight <= 20:
    price = 150
else:
    print("Too heavy (max 20 kg)")
    quit()

destination = input("Destination (bangkok or other): ")
if destination == "bangkok":
    price = price
elif destination == "other":
    price = price + 30
else:
    print("Unknown destination")
    quit()


express = input("Express (yes or no): ")

if express == "yes":
    price = price * 2

print(f"Shipping cost: {price}")
