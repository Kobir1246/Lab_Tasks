# Function to convert decimal to binary
def decimal_into_binary(decimal_1):  
    decimal = int(decimal_1)  
    return bin(decimal)[2:]  # [2:] to remove the '0b' prefix

# Function to convert decimal to octal
def decimal_into_octal(decimal_1):  
    decimal = int(decimal_1)  
    return oct(decimal)[2:]  # [2:] to remove the '0o' prefix

# Function to convert decimal to hexadecimal
def decimal_into_hexadecimal(decimal_1):  
    decimal = int(decimal_1)  
    return hex(decimal)[2:]  # [2:] to remove the '0x' prefix

# Driver code
decimal_1 = int(input("Enter the Decimal Number: "))  

binary = decimal_into_binary(decimal_1)
octal = decimal_into_octal(decimal_1)
hexadecimal = decimal_into_hexadecimal(decimal_1)

print(f"The given decimal number {decimal_1} in Binary is: {binary}")
print(f"The given decimal number {decimal_1} in Octal is: {octal}")
print(f"The given decimal number {decimal_1} in Hexadecimal is: {hexadecimal}")
