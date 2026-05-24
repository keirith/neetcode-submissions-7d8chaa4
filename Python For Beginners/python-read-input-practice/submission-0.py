def add_two_numbers() -> int:
    user_input = input()
    numbers = user_input.split(",")
    return int(numbers[0]) + int(numbers[1])


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())