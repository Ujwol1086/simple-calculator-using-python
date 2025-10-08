def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    if(b==0):
        return "Division by zero is not allowed."
    return a/b

def calculator():
    print("Select an option: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting the calculator")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            print("=========================")
            print("Addition")
            print(f"The Sum of {num1} and {num2} is: {add(num1, num2)}")
            print("=========================")
        elif choice == 2:
            print("=========================")
            print("Subtraction")
            print(f"The difference of {num1} and {num2} is: {subtract(num1, num2)}")
            print("=========================")
        elif choice == 3:
            print("=========================")
            print("Multiplication")
            print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")
            print("=========================")
        elif choice == 4:
            print("=========================")
            print("Division")
            if(num2 == 0):
                print("Division by zero is not allowed.")
                continue
            else:
                print(f"The division of {num1} and {num2} is: {divide(num1, num2)}")
            print("=========================")
if __name__ == "__main__":
    calculator()

