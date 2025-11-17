while True:
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nChoose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    print("Result:", result)

    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for using the calculator!")
        break
