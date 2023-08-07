#!/usr/bin/python3

def min_operations(n):
    """
    Calculate the fewest number of operations needed to obtain exactly n 'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
    """
    if n <= 1:
        return 0

    operations = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            operations = min(operations, i + min_operations(n // i))

    if operations == n:
        return n - 1

    return operations

if __name__ == "__main__":
    n = 9
    result = min_operations(n)
    print("Minimum number of operations:", result)

