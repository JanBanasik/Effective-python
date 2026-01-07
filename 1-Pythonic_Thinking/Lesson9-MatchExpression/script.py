RED = "red"
YELLOW = "yellow"
GREEN = "green"

# def take_match_action(light):
#     match light:
#         case RED:
#             print("Stop")
#         case YELLOW:
#             print("Slow down")
#         case GREEN:
#             print("Go!")

#         case _:
#             raise RuntimeError(f"Unknown light: {light}")

# take_match_action("red")
# take_match_action("yellow")
# take_match_action("green")

# take_match_action("blue")  # raises RuntimeError


# def take_truncated_action(light):
#     match light:
#         case RED:
#             print(f"{RED=} {light=}")
#             print("Stop")
# take_truncated_action(GREEN) # stop? wtf


import enum

class ColorEnum(enum.Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def take_enum_action(light):
    match light:
        case ColorEnum.RED:
            print("Stop")
        case ColorEnum.YELLOW:
            print("Slow down")
        case ColorEnum.GREEN:
            print("Go!")
        case _:
            raise RuntimeError(f"Unknown light: {light}")