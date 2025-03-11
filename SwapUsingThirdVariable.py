def swap(num1, num2):
    # Using a third variable
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2  # Return the swapped values

num1, num2 = 5, 10
print("Before Swap:", num1, num2)

num1, num2 = swap(num1, num2)  # Reassign the returned swapped values
print("After Swap:", num1, num2)
