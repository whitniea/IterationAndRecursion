def get_factorial_for_loop(n): 
    result = 1
    if n > 1:
        for i in range (1, n+1):
            result = result * i 
        return result
    else:
        return 'n has to be positive'
inp = input("enter a whole number:  ")
inp = int(inp)

print(f"the result is:{get_factorial_for_loop(inp)}")

def recur_factorial(n): 
    if n == 1: 
        return n 
    else:
        return n*recur_factorial(n-1)

num = input("please choose a number:  ")
if int(num) < 0: 
    print("factorial does not exist for negitive numbers")
elif num == 0:
    print("thhe factorial of 0 is 1")
else:
    print("the factorial of", num, "is", recur_factorial(num))