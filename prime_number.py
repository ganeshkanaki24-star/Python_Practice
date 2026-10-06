# print prime number in the range
n = int(input("Enter your Number: "))

for num in range(2, n):
    prime = True
    
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")






s = input()

words = s.split()

result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))















n = int(input())

for num in range(2, n):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
    