menu = {"pizza": 300, "popcorn": 200,"fried": 90,"soda": 60,"lemon water": 90}
cart = []
total = 0

print("Menu\n----------")

for item,price in menu.items():
    print(f"{item}:{price}")

while True:
    food = input("what food u need,(press q to stop): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is None:
        print("sorry, we dont have sell this")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food, end=" ")

print(f"total is RM{total}")