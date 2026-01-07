fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5
}

class OutOfBananas(Exception):
    pass

if (count := fresh_fruit.get("lemon", 0)) > 0:
    print(f"There are {count} lemons")
else:
    print(f"Out of stock of lemons")


slice_bananas = lambda n: n * 2  # each banana gives 2 pieces

def make_smoothies(pieces):
    if pieces > 0:
        return f"Made {pieces // 2} smoothies"
    else:
        raise OutOfBananas()
    
def make_cider(apples):
    return f"Made {apples // 4} ciders"

def make_lemonade(lemons):
    return f"Made {lemons} lemonades"
# make_smoothies = lambda pieces: f"Made {pieces // 2} smoothies" if pieces > 0 else (_ for _ in ()).throw(OutOfBananas()) tak sie nie pisze z tym throw

def out_of_stock():
    print("Cannot make smoothies: out of bananas!")

pieces = 0
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
    print(smoothies)
except OutOfBananas:
    out_of_stock()


if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get("apple", 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get("lemon", 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "Nothing to enjoy!"

print(f"{to_enjoy=}")

bottles = []

def pick_fruit():
    import random
    fruits = ["apple", "banana", "lemon", None]
    return random.choice(fruits)

while current_fresh_fruit := pick_fruit():  #
    
    for fruit, qty in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.append(batch)