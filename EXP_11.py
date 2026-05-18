def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
    else:
        print("Division successful! Result:", result)
    finally:
        print("Execution of divide_numbers completed.\n")

# Test cases
print("Case 1: 10 / 2")
divide_numbers(10, 2)
print("Case 2: 5 / 0")
divide_numbers(5, 0)
print("Case 3: '10' / 5")
divide_numbers("10", 5)