"""values = [4,2,9,2]
values.append(5)
print(values)
print(len(values),min(values),max(values),sum(values),values.count(2))
print(sorted(values))"""


""" min_value = values[0]
max_value = values[0]
for i in range(len(values)):
    if values[i] < min_value:
        min_value = values[i]
if values[i] > max_value:
        max_value = values[i]
print("Minimum value:", min_value)
print("Maximum value:", max_value)
"""

"""seen = set()
unique_items = []

for item in values:
    if item not in seen:
        seen.add(item)
        unique_items.append(item)

print(unique_items)  # [4, 2, 9, 5]"""

"""num = [4, 7, 9, 2]
unique_items = sorted(set(num))

if len(unique_items) >= 2:
    second_largest = unique_items[-2]
    print("Second largest value:", second_largest)"""


numbers = [10, 5, 21, 8, 20]
even = []
odd = []
for nums in range(len(numbers)):
    if numbers[nums] % 2 == 0:
        print(f"{numbers[nums]} is even")
        even.append(numbers[nums])
    else:
        print(f"{numbers[nums]} is odd")
        odd.append(numbers[nums])

print("Even numbers:", even)  
print("Odd numbers:", odd)  