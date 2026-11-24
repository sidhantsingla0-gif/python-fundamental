"""def add(a, b=0):
 return a + b
result = add(5, 3)
print(result)

def total(*numbers):
 return sum(numbers)

print(total(2, 3, 4))"""

"""def largest(a,b):
    if a>b:
        return a
    else:
        return b

print(largest(10, 20))"""
"""
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(prime(4))"""

"""def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum(2, 3, 4))"""


"""multiply = lambda x, y: x * y
print(multiply(5, 3))"""


'''celecius = [0, 10, 20, 30, 40, 100]
farhenite = list(map(lambda c: (c * 9/5) + 32, celecius))
print(farhenite)'''

'''words = ["apple", "banana", "cherry", "date"]
lengths = list(filter(lambda word: len(word) > 5, words))
print(lengths)'''