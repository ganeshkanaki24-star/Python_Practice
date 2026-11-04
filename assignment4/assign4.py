
# 1. Write a Python program to check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 2. Write a program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# 3. Write a program to check whether a given number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


# 4. Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

print()


# 5. Write a program to find the factorial of a number using a loop.

num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial is not possible")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial:", fact)


# 6. Write a program to reverse a string without using [::-1].

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


# 7. Write a program to check whether a string is a palindrome.

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 8. Write a program to count the number of vowels and consonants in a string.

text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# 9. Write a program to find the sum of all elements in a list.

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Sum of list:", total)


# 10. Write a program to find the largest and smallest element in a list without using max() or min().

numbers = [10, 50, 20, 5, 40, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 11. Write a program to remove duplicate elements from a list.

numbers = [10, 20, 10, 30, 20, 40, 50]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)


# 12. Write a program to count how many times each element appears in a list using a dictionary.

numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element Frequency:", frequency)


# 13. Write a program to find the second-largest number in a list.

numbers = [10, 20, 50, 40, 30]

largest = float('-inf')
second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Second largest number does not exist")
else:
    print("Second largest number:", second)


# 14. Write a program to sort a list without using sort() or sorted().

numbers = [40, 10, 50, 20, 30]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# 15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.

def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Even numbers:", even_numbers(numbers))


# 16. Write a program to find the frequency of each character in a string.

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:", frequency)


# 17. Write a program to check whether two strings are anagrams of each other.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")


# 18. Write a program to find all duplicate values in a list.

numbers = [10, 20, 30, 10, 40, 20, 50, 30]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values:", duplicates)


# 19. Write a program that takes a sentence and finds the longest word.

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# 20. Create a simple student marks program that:
#     1. accepts marks for 5 subjects,
#     2. calculates the total and percentage,
#     3. assigns a grade, and displays whether the student passed or failed.

marks = []

for i in range(1, 6):
    mark = int(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid Marks")

elif any(mark < 35 for mark in marks):
    print("Result: Fail")
    print("Grade: F")

else:
    print("Result: Pass")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: E")
