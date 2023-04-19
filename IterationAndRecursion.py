print("fractorial result using the iterative function")

def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result
def factorial_recursive(n)
    if n = 1:
        return 1
    else:
        return n * factorial_recursive(n)

def get_factorial_for_loop(n):
    result = 1 
    if n > 1:
        for i in range(1, n+1): 
            result = result * i 
        return result
    else:
        return 'n has to be positive'
inp = input("enter a number:  ")
inp = int(inp)
print(f"the result is: {get_factorial_for_loop(inp)}"


