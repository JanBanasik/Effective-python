single_with = (1,)
single_without = 1
single_another = (1,)

print(f"{type(single_with) is tuple=}")
print(f"{type(single_without) is int=}")
print(f"{type(single_another) is tuple=}")


value_a = (1,)  # No parentheses, right
list_b = [
    1,
]  # No parentheses, wrong
list_c = [(1,)]  # Parentheses, right
print("A:", value_a)
print("B:", list_b)
print("C:", list_c)
