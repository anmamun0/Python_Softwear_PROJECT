def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
num = 5
result = factorial(num)
print(result) # Output: 120

# Factorial Number Diferent-Way
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Example usage
num = 5
result = factorial(num)
print(result) # Output: 120
