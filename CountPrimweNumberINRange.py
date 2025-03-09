def  primeNUmber(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def inRange(start,end):
    primeNumber = [num for num in range(start,end+1) if primeNUmber(num)]
    return primeNumber
# Example Execution
start = 10
end = 50
result = inRange(start, end)
print("Prime numbers between", start, "and", end, ":", result)

        

        

        
        