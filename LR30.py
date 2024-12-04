# Function to calculate power using a loop
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Driver code
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")
