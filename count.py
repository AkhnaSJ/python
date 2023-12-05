x = int(input("Enter a number: "))
count = 0
while x != 0:
    x = x // 10
    count += 1
print("No: of digits: ",count)