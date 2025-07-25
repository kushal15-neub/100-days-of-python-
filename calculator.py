# Lets create a calculator:

from matplotlib.pylab import double


def add(x, y):
    return x + y


def subs(x, y):
    if x > y:
        return x - y
    else:
        return y - x


def mul(x, y):
    a = float(x)
    b = float(y)
    return a * b


def div(x, y):

    if x < y and y == 0:
        return "You cannot divide by zero"

    elif x > y and x == 0:
        return "You cannot divide by zero"
    else:
        g = double(x)
        h = double(y)
        return g / h


def mod(x, y):
    if x < y and y == 0:
        return "You cannot divide by zero"

    elif x > y and x == 0:
        return "You cannot divide by zero"
    else:
        g = double(x)
        h = double(y)
        return g % h


def pow(x, y):
    m = float(x)
    n = float(y)
    return m**n


def main():
    print("Welcome to the calculator")
    print(
        "You have operation addition (1), subtraction (2), multiplication (3), division (4), modulus (5), and power (6)"
    )

    x = float(input("Enter first number:"))
    y = float(input("Enter second number:"))

    choice = int(input("Enter your choices:"))

    if choice == 1:
        print("The sum is :", add(x, y))

    elif choice == 2:
        print("The difference is :", subs(x, y))

    elif choice == 3:
        print("The product is :", mul(x, y))

    elif choice == 4:
        print("The division is :", div(x, y))

    elif choice == 5:
        print("The modulus is :", mod(x, y))

    elif choice == 6:
        print("The power is :", pow(x, y))


if __name__ == "__main__":
    main()
