"""student1 = {"name": "Sidhant", "grade": "A", "marks": 85}
print(student1["name"])
print(student1.get("grade", "Not available"))
print(student1.get("marks", "Not available"))
student1["marks"] = 90
print(student1["marks"])
for key, value in student1.items():
    print(key, value)"""


"""set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("intersection:", set1.intersection(set2))"""

"""text = "Python is fun and learning Python is powerful"
words = text.lower().split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'learning': 1, 'powerful': 1}"""


"""list = [1, 2, 2, 4, 5]
for item in list:
    if list.count(item) > 1:
        remove_count = list.count(item) - 1
        for _ in range(remove_count):
            list.remove(item)
print(list)"""


items = [1, 2, 2, 4, 5]
unique_items = list(dict.fromkeys(items))
print(unique_items)  # [1, 2, 4, 5]