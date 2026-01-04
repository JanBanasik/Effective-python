snack_calories = {"chips": 140, "popcorn": 80, "nuts": 190}

items = list(snack_calories.items())
print(items)


item = ("Peanut butter", "Jelly")
first, second = item

print(f"{first} and {second}")


snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]

for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories")
