# String Indexing in Python

text = "Python"

print("String is:", text)

# positive indexing
print("First character:", text[0])
print("Second character:", text[1])
print("Third character:", text[2])

# negative indexing
print("Last character:", text[-1])
print("Second last character:", text[-2])
print("Third last character:", text[-3])

print("\nUsing for loop with positive indexing:")
for i in range(len(text)):
    print("Index", i, "=", text[i])

print("\nUsing for loop with negative indexing:")
for i in range(1, len(text)+1):
    print("Index", -i, "=", text[-i])