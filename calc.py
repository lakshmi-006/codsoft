def calculator():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        operation = input("choose operation(+,-,*,/_:")
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation. Please choose +,-,*,,or/.")
            return

        print(f"result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


calculator()
