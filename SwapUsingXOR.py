def swap(num1, num2):
    # Method 3 using XOR
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2

    return num1, num2  # Returns swapped values

# Initial values
num1, num2 = 5, 11
print("Before Swap:", num1, num2)

# Call function and store results
num1, num2 = swap(num1, num2)  # Update variables with swapped values

print("After Swap:", num1, num2)
