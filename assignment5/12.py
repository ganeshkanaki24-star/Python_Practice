# 12. Find the longest substring without repeating characters.

text = "abcabcbb"

seen = {}
start = 0
longest = ""

for i in range(len(text)):
    ch = text[i]

    if ch in seen and seen[ch] >= start:
        start = seen[ch] + 1

    seen[ch] = i

    if i - start + 1 > len(longest):
        longest = text[start:i + 1]

print("Longest substring:", longest)
