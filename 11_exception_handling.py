'''try:
 number = int(input("Enter an integer: "))
 result = 100 / number
except ValueError:
 print("Enter a valid integer.")
except ZeroDivisionError:
 print("Number cannot be zero.")
else:
 print(result)
finally:
 print("Finished.")'''

'''try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Enter valid integers.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Finished.")'''

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as ve:
    print(f"Invalid input: {ve}")
else:
    print(f"Your age is: {age}")
finally:
    print("Finished.")