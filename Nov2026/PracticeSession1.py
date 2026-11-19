text = "Python Programming"

print(text[0:6])
print(len(text))
print(text[-6:])
print(text[12:])

print(text[::2])

print(text[::-1])

value = "Welcome World"

print(value[::-1])
print(value[4:])  # ome World
print(value[:13:2])  # Wce od value[0:length:2-1] skipping 1 char

print(value[:-2])  # value[0:length-2],

print(value[-13:-1])

name = "Hello, Python!"
print(len(name))
print(name[-6:-1])  # ython!

print((name[::2]))  # Hlo yhn
print(name[7:])  # Python!
print(name[:5])  # Hello

print(name[::3])  # Skips 2 chars and print as,  Hl tn
print(name[::-1])

sentance2 = " i lover Python Programming "

print(sentance2.strip().title())
print(sentance2.count('o'))

sentance3 = "Coding in Python is fun"

print(sentance3.replace("fun", "awsome"))
print(sentance3.index('Python'))
print(sentance3.upper())


sentance4 = "My Name is Praneeth 36 years old, still coding and learning is my habbit"
vowels = ['a', 'e', 'i', 'o', 'u']
sum = 0
for words in sentance4.lower():
    if words in vowels:
        sum += 1
print(f"There are {sum} number of Vowels in the given sentence")


inputString = "Madam"#level

if inputString.lower() == inputString[::-1].lower():
    print(f"{inputString} is a Palindrome")
else:
    print(f"{inputString} is not a Palindrome")