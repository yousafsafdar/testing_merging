def cube(number):
    return number * number * number


def square():
    return 2 * 5

def only_print():
    print("just checking")


def add_number(any_number):
    return any_number + 10


def by_three(divisible):
    if divisible % 3 == 0:
        result = cube(divisible)
        calling_square = square()
        only_print()
        five_times_result = add_number(calling_square)
        return result, calling_square, five_times_result
    else:
        return False


def main():
    input_giving = by_three(9)
    print(input_giving)

main()