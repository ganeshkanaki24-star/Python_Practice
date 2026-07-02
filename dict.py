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

