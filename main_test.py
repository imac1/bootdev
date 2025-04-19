from main import Dragon, Unit, Rectangle

run_cases = [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -2, -3, 0, 0, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 0, 1, 1, 0, True),
    (Dragon("Gold Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
    (Dragon("Gold Dragon", 0, 0, 20, 20, 20), 10, 10, 20, 20, True),
]

submit_cases = run_cases + [
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), 0, 0, 10, 10, False),
    (Dragon("Black Dragon", 5, -1, 3, 2, 2), -10, -10, 10, 10, True),
]


def test(dragon, input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f" * Dragon pos_x: {dragon.pos_x}")
    print(f" * Dragon pos_y: {dragon.pos_y}")
    print(f" * Dragon height: {dragon.height}")
    print(f" * Dragon width: {dragon.width}")
    print("")
    print(f" * Area x1: {input1}")
    print(f" * Area y1: {input2}")
    print(f" * Area x2: {input3}")
    print(f" * Area y2: {input4}")
    print("")
    result = dragon.in_area(input1, input2, input3, input4)
    print(f"Expected in area: {expected_output}")
    print(f"Actual in area:   {result}")
    if result == expected_output:
        return True
    return False


def main():
