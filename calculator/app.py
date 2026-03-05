from calculator.core import add, subtract, multiply, divide, clear

def calculate(a, operator, b=None):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    elif operator == "C":
        return clear()
    else:
        raise ValueError("Invalid operator")