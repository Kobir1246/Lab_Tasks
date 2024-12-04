from operator import add

lt1 = [4, 8, 12, 16, 20, 24]  
lt2 = [2, 4, 6, 8, 10, 12]  

# Display the original items of the lists lt1 and lt2  
print("Display the elements of List 1: " + str(lt1))  
print("Display the elements of List 2: " + str(lt2))  

# Use map() function with add operator to add the elements of the lists lt1 and lt2  
res_lt = list(map(add, lt1, lt2))  # Pass the lt1, lt2 and add as the parameters  

# Display the sum of the two lists  
print("Sum of the list 1 and list 2 is: " + str(res_lt))  
