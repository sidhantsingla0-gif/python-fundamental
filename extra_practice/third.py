# name =  input("enter your name: ")

# print(f"good morning {name}")

letter = ''' Dear <|name|>
your are selected
<|date|>'''

print(letter.replace("<|name|>", "sid").replace("<|date|>","2 feb 2026"))