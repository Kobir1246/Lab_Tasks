# Function to remove duplicates from a list
def remove_duplicates(input_list):
    # Using a set to track seen elements
    seen = set()
    output_list = []
    
    for item in input_list:
        if item not in seen:
            output_list.append(item)
            seen.add(item)
    
    return output_list

# Example usage
input_list = [1, 2, 3, 2, 4, 1, 5]
output_list = remove_duplicates(input_list)
print("Original List:", input_list)
print("List without duplicates:", output_list)
