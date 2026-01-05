def fail():
    return Exception("Oops")


x = fail() if False else 42
print(x)

print(1 and "even")


def my_long_function_call(a, b, c):
    return f"Long function called with {a}, {b}, {c}"


def my_other_long_function_call(d, e, f):
    return f"Other long function called with {d}, {e}, {f}"


i = 3
x = (
    my_long_function_call(1, 2, 3)
    if i % 2 == 0
    else my_other_long_function_call(4, 5, 6)
)




x = 2
y = 1


if x and (z := x > y):
    print(f"{x} is greater than {y}")


if x and z := x > y:
    print(f"{x} is greater than {y}")