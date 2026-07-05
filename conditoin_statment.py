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


print("---------------------------------------------------")


# check if a username and password are correct to allow access to a system
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "admin123":
    print("Access granted.")
else:
    print("Access denied. Invalid username or password.")

# display action based on the traffic light color
traffic_light = input("Enter the traffic light color (red/yellow/green): ")
if traffic_light == "red":
    print("Stop.")
elif traffic_light == "yellow":
    print("Prepare to stop.")
elif traffic_light == "green":
    print("Go.")
else:
    print("Invalid traffic light color.")

# atm amont withdrawl
balance = 5000
withdrawal_amount = int(input("Enter the amount to withdraw: "))
if withdrawal_amount > balance:
    print("Insufficient balance.")
elif withdrawal_amount % 100 != 0:
    print("Please enter an amount in multiples of 100.")
else:
    balance = balance - withdrawal_amount
    print("Withdrawal successful. Remaining balance:", balance)
'''
a = [1,2,3,4]
b = [3,4,5]
for i in a:
    if i in b:
        print(i)
    
