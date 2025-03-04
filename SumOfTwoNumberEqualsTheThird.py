# If the sum  of any two numbers are equals the third number print"Sum of two numbers equals the third number"
def checkNumbers(a,b,c):
    if a + b == c or a + c == b or b + c == a:
        print("Sum of two numbers are equals  the third number.")
a,b,c=5,4,1
checkNumbers(a,b,c)