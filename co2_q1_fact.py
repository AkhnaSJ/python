x = int(input("Enter a number: "))
fact = 1
if (x == 0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,x+1):
        fact *= i
    print(f"Factorial of {x} is {fact}")