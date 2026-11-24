"""words = "piython"
print(words[0])
print(words[-1])
print(words[1:4])
print(words[4:1:-1])

vowel_count = sum(words.count(v) for v in "aeiou")
print("Vowel count:", vowel_count)  # 1 (just 'o')"""



word = "    racecar     "
"""is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")"""

"""for i in range(len(word)):
    print(f"frequency of the character '{word[i]}' in '{word}' is {word.count(word[i])}")"""

print("words.strip():", word.strip())
print("words.lstrip():", word.lstrip())
print("words.rstrip():", word.rstrip())
print("words.title():", word.title())