# 14. Group a list of strings into anagram groups.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = tuple(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

result = list(groups.values())

print("Anagram groups:", result)
