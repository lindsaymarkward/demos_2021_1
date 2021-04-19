"""Do this now:
Write a function that takes a list of numbers
and display all of the negative, and positive
numbers in two separate groups.
"""


def main():
    numbers = [3, 5, 90, -1, 23, -123, 0, 0, 40, -1]
    display_in_groups(numbers)


def display_in_groups(numbers):
    print("Negative: ")
    negative_numbers = [number for number in numbers if number < 0]
    print(negative_numbers)
    print("Positive: ")
    positive_numbers = [number for number in numbers if number > 0]
    print(positive_numbers)


if __name__ == '__main__':
    main()
