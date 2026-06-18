import numpy as np

try:
    arr = np.array([1, 2, 3, 4])

    print("NumPy Array:", arr)
    print("Accessing element:", arr[10])

except IndexError:
    print("Exception occurred: Invalid index in NumPy array")