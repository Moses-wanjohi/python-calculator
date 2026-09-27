from calculator import Calculator

def print_menu():
    print("\n--- Python Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Exit")

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    calc = Calculator()

    while True:
        print_menu()
        choice = input("Select an operation (1-6): ").strip()

        if choice == '6':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5',):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter secend number: ")

            try:
                if choice == '1':
                    result = calc.add(num1, num2)
                    op = "+"
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    op = "-"
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    op = "*"
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    op = "/"
                elif choice == '5':
                    result = calc.power(num1, num2)
                    op = "^"

                print(f"\nResult: {num1} {op} {num2} = {result}")

            except ValueError as err:
                print(f"\nError: {err}")

        else:
            print("Invalid choice. Please pick 1 through 6.")

if __name__ == "__main__":
    main()

                   

                   



