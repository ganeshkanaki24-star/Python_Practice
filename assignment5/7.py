# 7. Check whether two strings are anagrams without using sorted().

str1 = "listen"
str2 = "silent"

frequency = {}

for ch in str1:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in str2:
    frequency[ch] = frequency.get(ch, 0) - 1

if all(value == 0 for value in frequency.values()):
    print("Anagrams")
else:
    print("Not Anagrams")