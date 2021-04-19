"""Do this now:
Write a function to get a valid age from a user
Write two lines of main code to show its use
"""
MAXIMUM_AGE = 130


def main():
    """Program for getting ages."""
    age = get_valid_age()
    print(f"You are {age} years old!")


def get_valid_age():
    """Get a valid age between 0 and MAXIMUM_AGE."""
    age = int(input("Age: "))
    while age < 0 or age > MAXIMUM_AGE:
        print("Invalid age")
        age = int(input("Age: "))
    return age


main()
