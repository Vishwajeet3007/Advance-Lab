# If any two numbers are same print "Two numbers are same." and Display the largest number.
def equalNumbersAndLargest(a,b,c):
    if a == b  or b==c or a==c:
        print("Two numbers are equal.")
        if a >= b and a >= c:
            print(f"{a} is greater.")
        elif b >= c and b >= a:
            print(f"{b} is greater.")
        else:
            print(f"{c} is greater.")
a,b,c=5,8,5
equalNumbersAndLargest(a,b,c)