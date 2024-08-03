try:
    number=int(input("Enter the number:"))
    divisor=int(input("Enter the divisor:"))
    result = number / divisor
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Division successful:", result)
finally:
    print("Execution completed.")