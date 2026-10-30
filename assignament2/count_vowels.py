# Count Vowels
# Write a function that counts the vowels in a string.

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count

text = input("Enter a string: ")

print("Total vowels:", count_vowels(text))