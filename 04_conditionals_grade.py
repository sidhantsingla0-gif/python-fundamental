"""marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = 'A'
elif marks >=80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = "Marks need to be improved"
print(f"Your grade is: {grade}")"""


"""num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print(f"the largest number is :{num1 if(num1 > num2 and num1 > num3) else (num2 if(num2 > num3) else num3)}")


