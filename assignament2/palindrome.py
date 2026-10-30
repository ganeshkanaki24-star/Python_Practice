# Palindrome Checker
# Write a function that returns True if a string is a palindrome.
def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")

print(palindrome(word))