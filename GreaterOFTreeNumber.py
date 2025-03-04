def greaterOfThreeNumber(a,b,c):
    if a >= b and a >= c:
        print(f"{a} is greater than {b} and {c}")
    elif b >= a and b >= c:
        print(f"{b} is greater than {a} and {c}")

    else:
        print(f"{c} is greater than {a} and {b}")
a=5
b=4
c=8
greaterOfThreeNumber(a,b,c)