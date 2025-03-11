def swap(num1, num2):
    # Method 4: Using Arithmetic Operations
    num1 = num1 * num2
    num2 = num1 // num2
    num1 = num1 // num2

    return num1, num2  # Return the swapped values

num1, num2 = 5, 10
print("Before Swap:", num1, num2)

num1, num2 = swap(num1, num2)  # Reassign swapped values
print("After Swap:", num1, num2)
