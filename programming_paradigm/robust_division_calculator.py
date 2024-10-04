def safe_divide(numerator, denominator):
    try:
        divide = float(numerator) / float(denominator)
        return f"The result of the division is {divide}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")