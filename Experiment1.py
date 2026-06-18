print("Control Flow Statements")
a = int(input("Enter a number: "))

if a > 0:
    print("Positive")

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

if a > 0:
    print("Positive number")
elif a < 0:
    print("Negative number")
else:
    print("Zero")

print("For loop")
for i in range(5):
    print(i)

print("While loop")
i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Break example")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("Continue example")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)