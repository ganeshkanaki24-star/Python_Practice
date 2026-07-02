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