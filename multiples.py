x = int(input("Enter a number: "))
n = int (input("Enter the limit: "))

print("The multiples of x are: ")
for i in range(1,n+1):
    m = x*i
    print(m, end=' ')