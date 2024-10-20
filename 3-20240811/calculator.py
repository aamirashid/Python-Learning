print("Basic Calculator by using Def Function")
def calculator():
    choice = input("Press any operation key: [ +  -  *  / ] : ")

    if choice in ['+', '-', '*', '/']:
        print(f"Enter two values for {choice}")
        num1 = float(input("First value: "))
        num2 = float(input("Second value: "))
        if choice == '+':
            sum = num1 + num2
            print(f"Sum of {num1} + {num2} is {sum:.2f}")
        elif choice == '-':
            print(f"Subtraction of {num1} - {num2} is {num1-num2}")
        elif choice == '*':
            print(f"Multiplication of {num1} * {num2} is {num1*num2}")
        elif choice == '/':
            print(f"Division of {num1} / {num2} is {num1/num2}")
    else:
        print("Wrong selection")

calculator()            # Execution of calculator