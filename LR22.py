# Function to calculate the sum of first N natural numbers
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2  # Formula for the sum of first N natural numbers

# Driver code
n = 10  # First 10 natural numbers
result = sum_of_natural_numbers(n)
print("Sum of the first 10 natural numbers is:", result)
