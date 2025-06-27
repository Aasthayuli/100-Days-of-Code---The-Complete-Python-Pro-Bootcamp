
import art

print(art.logo)


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : divide
}


def calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()





calculator()