num = int(input("Enter a number: "))
for i in range(1, 6):
    if num == i:
        j = 1
        while j <= 10:
            print(f"{i} x {j} = {i * j}")
            j += 1

        break
else:
    print("The number is not between 1 and 5.") 
