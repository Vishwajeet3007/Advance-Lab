numbers = input("Enter numbers separated by spaces: ").split()

for num in numbers:
    num = int(num)
    rev_num = 0
    
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    
    print("Reversed number:", rev_num)
