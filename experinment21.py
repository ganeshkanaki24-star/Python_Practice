#shallow copy
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100

print("Original:", original)
print("Shallow:", shallow)

#deep copy
import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print("Original:", original)
print("Deep:", deep)