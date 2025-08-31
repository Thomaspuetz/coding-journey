# Loops and lists combined

num_items = int(input("How many items do you want? "))

shopping_list = []

for i in range(num_items):
    item = input(f"Enter item {i+1}: ")
    shopping_list.append(item)

print("\n Your Shopping List: ")
for item in shopping_list:
    print("-", item)
