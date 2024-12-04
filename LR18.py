# Function for calculating A raised to the power B
def power_1(A, B):  
    if B == 0:  
        return 1  
    if B % 2 == 0:  
        half_power = power_1(A, B // 2)  # Avoid recalculating the same power
        return half_power * half_power  
    return A * power_1(A, B // 2) * power_1(A, B // 2)  # Fixed the recursive call

# Function for calculating the number of digits (order) in the number A
def order_1(A):  
    N = 0  
    while A != 0:  
        N += 1  
        A = A // 10  
    return N  

# Function to check if the given number is an Armstrong number
def is_Armstrong(A):  
    N = order_1(A)  
    temp_1 = A  
    sum_1 = 0  
        
    while temp_1 != 0:  
        R_1 = temp_1 % 10  
        sum_1 += power_1(R_1, N)  
        temp_1 = temp_1 // 10  
    
    return sum_1 == A  # Return true if sum equals the original number

# Driver code
A = int(input("Please enter the number to be checked: "))  
print(is_Armstrong(A))
