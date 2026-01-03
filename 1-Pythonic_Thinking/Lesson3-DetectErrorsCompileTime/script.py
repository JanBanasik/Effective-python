def bad_reference():
    print(x)
    x = 5


# bad_reference()
# This will raise an UnboundLocalError because 'x' is referenced before assignment.
# But only when the function is called, not at compile time.


def sometimes_ok(x):
    if x:
        my_var = 123
    print(my_var)


sometimes_ok(True)
# sometimes_ok(False)
# This will raise a NameError if called with False, because 'my_var' is not defined in that case.


def bad_math():
    return 1 / 0


# bad_math()
# This will raise a ZeroDivisionError when the function is called, not at compile time.
