from sklearn.linear_model import LinearRegression
import numpy as np
'''
x = np.array([20, 25, 30]).reshape(-1, 1)
y = np.array([100, 150, 200])

model = LinearRegression()
model.fit(x, y)

print(model.predict([[40]]))
'''
'''
x = np.array([1,2,3,4]).reshape(-1,1)
y = np.array([10,20,30,40])

model = LinearRegression()
model.fit(x, y)
print(model.predict([[10]]))
'''
# product price prediction 
x = np.array([1,2,3,4]).reshape(-1, 1)
y = np.array([15000, 17000, 19000, 21000])

model = LinearRegression()
model.fit(x, y)
print(model.predict([[5]]))