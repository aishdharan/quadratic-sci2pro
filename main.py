import os
import sys
import math


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    x1 = complex((- b + math.sqrt(discriminant)) / (2 * a))
    x2 = complex((- b - math.sqrt(discriminant)) / (2 * a))
    return x1, x2
 """Calculate is a function created by keyword 'def' to solve the given variables which are of type 'float'.
    Parameters are taken of type 'float'
    Return is of the type 'float'
    """

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    # return value of exit status
    return os.EX_OK


if __name__ == "__main__":
    # exit status went to os
    sys.exit(main())
