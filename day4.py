# cocktails = []

# while True:

# drink = input("Enter a cocktail (or type 'done' to finish): ")
# if drink.lower() == "done":
# break
# cocktails.append(drink)

# if cocktails:
# print(f"Your cocktail lineup tonight is: {', '.join(cocktails)}")
# else:
# print("You didn't add any cocktails!")
import random

cocktails = []

while True:
    drink = input("Enter a cocktail (or type 'done' to finish): ")
    if drink.lower() == "done":
        break
    cocktails.append(drink)

num_guests = int(input("How many people are coming? "))

random.shuffle(cocktails)

for i in range(num_guests):
    cocktail = cocktails[i % len(cocktails)]
    print(f"Guest #{i+1} gets a {cocktail}")
