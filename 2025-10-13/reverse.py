import yogi


def ndigits(n: int) -> int:
    """Returns the number of digits in n.
    Args:
        n: The integer to count digits (n >= 0)
    """
    ndigits = 1
    while n >= 10:
        n //= 10
        ndigits += 1
    return ndigits


def reverse(n: int) -> int:
    """Returns an integer whose digits are the reverse of n's digits. 
    The trailing zeros are lost. In case the number must be printed with
    leading zeros, use str.reverse(n).zfill(ndigits(n)).
    Args:
        n: The integer to reverse (n >= 0)
    """
    r = 0  # The reversed number
    while n > 0:
        r = r * 10 + (n % 10)
        n //= 10
    return r
