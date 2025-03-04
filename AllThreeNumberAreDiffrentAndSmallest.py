# If all three numbers are diffrent print "All numbers are difffrent." and Display the smallest number.
def DiffrentNumberAndSmallest(a,b,c):
    if a != b and b != c and c != a:
        print("All numbers are diffrent.")
        if a <= b and a <= c:
            print(f"{a} is smallest number.")
        elif b <= c and b <= a:
            print(f"{b} is smallest number.")
        else:
            print(f"{c} is smallest number.")
    
a,b,c = 4,6,6
DiffrentNumberAndSmallest(a,b,c)