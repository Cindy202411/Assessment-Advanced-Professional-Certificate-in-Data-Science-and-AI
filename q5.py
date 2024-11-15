def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
 if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):

        return "Both num and divisor must be numeric."

    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
# Scenario 1: 10, 2

result1 = check_divisibility(10, 2)

print(f"Is 10 divisible by 2? {result1}")

#Is 10 divisible by 2? True


# Scenario 2: 7, 3

result2 = check_divisibility(7, 3)

print(f"Is 7 divisible by 3? {result2}")

#Is 7 divisible by 3? False
