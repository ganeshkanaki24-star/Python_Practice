# 16. Check whether a given string contains balanced parentheses using a stack.

text = "{[()]}"

stack = []

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

balanced = True

for ch in text:
    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":
        if not stack or stack[-1] != pairs[ch]:
            balanced = False
            break

        stack.pop()

if balanced and len(stack) == 0:
    print("Balanced Parentheses")
else:
    print("Not Balanced")