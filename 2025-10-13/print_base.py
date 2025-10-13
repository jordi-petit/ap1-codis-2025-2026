import yogi


def print_base(n: int, b: int) -> None:
    """Prints the integer n in base b.
    Args:
        n: The integer to print (n >= 0)
        b: The base to print in. Must be between 2 and 10, inclusive.
    """
    if n < b:  # Base case
        print(n, end="")
    else:  # Recursive case
        print_base(n // b, b)
        print(n % b, end="")


def print_base_short(n: int, b: int) -> None:
    """Prints the integer n in base b.
    Args:
        n: The integer to print (n >= 0)
        b: The base to print in. Must be between 2 and 10, inclusive.
        
    Comment: This is a shorter version using a single if statement.
    """

    if n >= b:
        print_base(n // b, b)
    print(n % b, end="")


if __name__ == "__main__":
    n = yogi.read(int)
    b = yogi.read(int)
    print_base(n, b)
    print()
    print_base_short(n, b)
    print()
