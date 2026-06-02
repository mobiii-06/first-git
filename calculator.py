def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    print("addition", a + b)
    print("subtraction", a - b)
    print("multiplication", a * b)
    if b != 0:
        print("division", a / b)
    else:
        print("division", "undefined (cannot divide by zero)")


if __name__ == "__main__":
    main()