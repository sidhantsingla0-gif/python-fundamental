lines = [
        "this is a test",
        "this is my life",
        "this is my world",
    ]

with open("output.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.writelines(line + "\n")

try:
        with open("output.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        print("".join(lines))  # prints the full file content

        print("Total lines:", len(lines))

except FileNotFoundError:
        print("output.txt was not found.")


    
'''new_entry = "this is my love"
with open("output.txt", "a", encoding="utf-8") as file:
        file.writelines(new_entry + "\n")

with open("output.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("".join(lines))'''

'''try:
    with open("123.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("".join(lines))

except FileNotFoundError:
     print("123.txt was not found.")'''