# 6. Find the first non-repeating character in a string.

text = "programming"

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")