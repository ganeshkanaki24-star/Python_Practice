# Different String Operations in Python

str1 = "Hello"
str2 = "Python"

# 1. Concatenation
print("Concatenation:", str1 + " " + str2)

# 2. Repetition
print("Repetition:", str1 * 2)

# 3. Length of string
print("Length of str1:", len(str1))

# 4. Upper case
print("Upper case:", str1.upper())

# 5. Lower case
print("Lower case:", str2.lower())

# 6. Indexing
print("First character of str1:", str1[0])

# 7. Slicing
print("Slicing of str2:", str2[0:3])

# 8. Replace
print("Replace:", str2.replace("Python", "World"))

# 9. Checking string
print("Is str1 alphabetic?", str1.isalpha())

# 10. Comparison
if str1 == str2:
    print("Both strings are same")
else:
    print("Both strings are different")