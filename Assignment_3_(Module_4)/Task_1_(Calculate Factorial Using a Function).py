def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

def fact(n):
    num = 1
    for i in range(1,n+1):
        num = num * i
    return num

n = int(input("Enter a number: "))
f = factorial(n) # or fact(n) use any one function
print("Factorial of", n, "is:", f)



