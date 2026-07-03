''''
# Factorial of 5 number using fuction
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
    return fact
result = factorial(5)
print(result)

# fibonacci 
def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a, end=' ')
        c = a + b
        a = b
        b = c
fibonacci(10)

print("-------------------------------------------------------------------")

# take user input into lowercase and convert lowercase to uppercase using function

def convert_upper(text):
    return text.upper()

name = input("Enter a string in lowercase: ")

result = convert_upper(name)

print("Uppercase String:", result)
'''
# lambda
num = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, num))
print(squared)

# lambda for upper case conversion
names = ["ganesh", "dd", "vijay"]
upper = list(map(lambda x : x.upper(), names))
print(upper)


# less than 40 find out of list using lambda
numbers = [10, 20, 30, 40, 50, 60, 33, 40, 50]
n = list(filter(lambda x : x < 40, numbers))
print(n)

# find secong largest number in list using function
def second_largest(num):
    num.sort()
    return num[-2]
print(second_largest([10, 20, 30, 40, 50, 60, 33, 40, 50]))

# another way
def second_largest(num):
    return sorted(set(num))[-2]
print(second_largest([10, 20, 30, 40, 50]))

# find the even or odd number using lambda fuction 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even = list(filter(lambda x : x % 2 == 0, num))
print(even)
                     


# positive number find out of list using lambda
num = [-10, 20, -30, 40, -50, 60, -33, 40, -50]
positive = list(filter(lambda x : x > 0, num))
print(positive)

# find of AEIOU in string using lambda
string = "i am the ganesh python programmer"
n = list(filter(lambda x : x in 'aeiou', string))
print(n)

# another way using function 
def xyz(str):
    vowesl = 'aeiouAEIOU'
    count = 0
    for i in str:
        if i in vowesl:
            count += 1
    return count
print(xyz("I am the gAnesh python prOgrammer"))

