try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2 # Might raise ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
  
  print("Error: Cannot divide by zero!")
except ValueError:
  print("Error: Invalid input! Please enter numbers only.")
except Exception as e:
  print("An unexpected error occurred:", e)