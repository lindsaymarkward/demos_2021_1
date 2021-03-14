"""Do this now:
Write a function to get a valid age from a user
Write two lines of main code to show its use
"""


def main():
    age = get_valid_age()
    print(f"You are {age} years old!")


def get_valid_age():
    age = int(input("Age: "))
    while age < 0 or age > 100:
        print("Invalid age")
        age = int(input("Age: "))
    return age


main()
