numbers = []
input1 = float(input("Enter a number: "))
input2 = float(input("Enter a number: "))
numbers.append(input1)
numbers.append(input2)
result = input1 + input2
print("sum:", result)
for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)
    total = sum(numbers)
    print("Sum:", total)

print (numbers)








