'''
# multiple condition statement
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Enter only positive number")

print("---------------------------------------------------")
'''
# voting eligibility using is true or false
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    voterId = input("Enter you have voter id (yes/no): ")
    if voterId == "yes":
        print("You can vote.")
    else:
        print("You need a voter ID to vote.")
else:
    print("You are not eligible to vote.")


