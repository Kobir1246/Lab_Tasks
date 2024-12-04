# Function to reverse a string
def reverse_string(s):
    return s[::-1]  # Slice the string in reverse order

# Driver code
input_string = input("Please enter a string: ")
print("Reversed string:", reverse_string(input_string))