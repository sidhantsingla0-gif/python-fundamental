'''cubes = [x**3 for x in range(1, 11)]
print(cubes)
'''
'''words = ["apple", "banana", "orange", "date"]
vowels = [word for word in words if word and word[0].lower() in "aeiou"]

print(vowels)  # ['apple', 'orange']'''

'''nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5]'''

even_odd = ["even" if x % 2 == 0 else "odd" for x in range(1, 21)]
count_even = even_odd.count("even")
count_odd = even_odd.count("odd")
print(even_odd)
print("Count of even numbers:", count_even)
print("Count of odd numbers:", count_odd)