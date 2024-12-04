def manage_customers():
    # Initial list of customers
    customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
    
    # a. Access the third customer in the list and print their name
    third_customer = customers[2]
    print("Third customer:", third_customer)
    
    # b. Change the name of the second customer to "Ben"
    customers[1] = "Ben"
    
    # c. Add a new customer named "Frank" to the end of the list
    customers.append("Frank")
    
    # d. Remove the customer "David" from the list
    customers.remove("David")
    
    # e. Sort the customer names alphabetically and print the final list
    customers.sort()
    print("Final sorted customer list:", customers)

# Call the function
manage_customers()
