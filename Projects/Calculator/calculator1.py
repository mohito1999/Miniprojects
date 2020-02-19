try_again = "yes"

while try_again == "yes":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Select an operation: ")


    if operation == "1":
        print(num1 + num2)
    elif operation == "2":
        print(num1 - num2)
    elif operation == "3":
        print(num1 * num2)
    elif operation == "4":
        print(num1 / num2)
    try_again = input("Would you like to try again?")

    if try_again == "no":
        print("Thanks for using!")
