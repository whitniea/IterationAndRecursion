from math import factorial

print("fractorial result using the iterative function")

n = int(input("enter a number:  "))

factorial = 1

if n < 0:    
    print("factors do not exist for negitive numbers.")
elif n == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,n + 1):
        factorial = factorial*i
    print("the factorial of ",n," is ", factorial)
for i in range(n):
    print(i)

def factorial(n):
    if n == 1:
        return 1 
    else:
        return (n * factorial(n-1))

num = 3 
print("the factorial of ", num, " is ", factorial(num))