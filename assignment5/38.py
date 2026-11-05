# 38. Generate all permutations of a given string or array without duplicates.

def permutations(text):

    result = []

    def backtrack(path, remaining):

        if len(remaining) == 0:

            result.append(path)
            return

        used = set()

        for i in range(len(remaining)):

            ch = remaining[i]

            if ch in used:
                continue

            used.add(ch)

            new_remaining = remaining[:i] + remaining[i + 1:]

            backtrack(path + ch, new_remaining)


    backtrack("", text)

    return result


text = "AAB"

print("Permutations:", permutations(text))