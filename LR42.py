# Function to count occurrences of a substring
def count_substring(main_string, sub_string):
    return main_string.count(sub_string)

# Input from the user
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to find: ")

# Count and display the result
occurrences = count_substring(main_string, sub_string)
print(f'The substring "{sub_string}" occurred {occurrences} times in the string.')
