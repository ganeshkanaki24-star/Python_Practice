nasted_dic = {
    'person' : {'name': 'jhon', 'age': 31},
    'address' : {'city': 'New York', 'zip': '1001'}
}

nasted_dic['person']['age'] = 35
print(nasted_dic)

# copy in dictionery

Original_dict = {'name': 'jhon'}
copied_dict = Original_dict.copy()
copied_dict['name'] = 'jane'
print("Original:", Original_dict)
print("Copied:", copied_dict)


# marge the dictionery
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)

# squere the values in dictionery
square_dict ={
    'a':1,
    'b':2,
    'c':3
}
print({k:v**2 for k,v in square_dict.items()})


dict_comp ={k:k for k in range(0,10) if k<=4}
print(dict_comp)

#Employee salary increament by 10%
#increase salary by 10%
salary = {
    'A' : 30000,
    'B' : 40000
}
for emp in salary:
    salary[emp] += salary[emp] * 0.10

print(salary)

#Shopping cart calculate total price
cart = {"Laptop": 50000, "Mouse": 500}
price = sum(cart.values())
print(price)

# invertor management 
#scenario update stock after sale
stock = {"pen": 20}
sold = {"pen": 5}
for k in sold:
    stock[k] -= sold[k]

print(stock)

#string character change using update dont use replace method
a = "Sveri"
a = a.replace("S", "P")
print(a)

# without using in-build functions sort
a = [1, 3, 7, 8, 6, 4]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

