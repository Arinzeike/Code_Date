num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
option = input("Enter option: ")
if option == "+":
    print(num1 + num2)
elif option == "-":
    print(num1 - num2)
elif option == "/":
    print(num1 / num2)
elif option == "*":
    print(num1 * num2)
else:
    print("IVALID OPTION")
    print("TRY AGAIN")