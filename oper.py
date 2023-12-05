x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))
print("1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division: ")
choice = int(input("Enter your choice: "))

if choice == 1:
    result = x + y
    print("Sum : ",result)

elif choice == 2:
    result = x - y
    print("Difference : ",result)

elif choice == 3:
    result = x * y
    print("Product : ",result)

elif choice == 4:
    result = x // y
    print("Quotient : ",result)

else: 
    print("Invalid Choice: ")


