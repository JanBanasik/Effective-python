from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

print(my_values)  # {'red': ['5'], 'blue': ['0'], 'green': ['']}
print(repr(my_values))  # {'red': ['5'], 'blue': ['0'], 'green': ['']}

print(f"Red: {my_values.get('red')}")
print(f"Green: {my_values.get('green')}")
print(f"Opacity: {my_values.get('opacity')}")

print(f"-" * 20)

red = int(my_values.get("red", [""])[0] or 0)
green = int(my_values.get("green", [""])[0] or 0)
opacity = int(my_values.get("opacity", [""])[0] or 0)

print(f"Red: {red}")
print(f"Green: {green}")
print(f"Opacity: {opacity}")


def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default


red = get_first_int(my_values, "red")
green = get_first_int(my_values, "green")
opacity = get_first_int(my_values, "opacity")

print(f"-" * 20)
print(f"Red: {red}")
print(f"Green: {green}")
print(f"Opacity: {opacity}")
