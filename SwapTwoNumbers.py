def swap(num1, num2):
    # Method 1: Without using a third variable (using addition & subtraction)
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    # Method 2: Using Arithmetic Operations
    num1 = num1 * num2
    num2 = num1 // num2
    num1 = num1 // num2

    # Method 3Using a third variable
    temp = num1
    num1 = num2
    num2 = temp

    # Method 4 using XOR
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2




    return num1, num2  # Return swapped values

num1, num2 = 5, 10
print("Before Swap:", num1, num2)

num1, num2 = swap(num1, num2)  # Reassign swapped values
print("After Swap:", num1, num2)
