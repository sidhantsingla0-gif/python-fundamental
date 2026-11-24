"""for number in range(1,6):
    print(number)
print("Done")


count = 2
while count <= 10:
    print(count)
    count += 1"""

"""for num in range (1,50):
    if num %2 == 0:
        print(num)"""

#num = int(input("Enter a number: "))

"""if num < 0:
    print("factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")"""


"""for i in range(1,11):
    print(f"{num} x {i} = {num*i}")"""

# upper right triangle
"""rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


# down right triangle
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print("*" * i)"""


#cross pattern
n = 5

for r in range(n):
    for c in range(n):
        if r == c or r + c == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()