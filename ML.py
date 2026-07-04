from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([20, 25, 30]).reshape(-1, 1)
y = np.array([100, 150, 200])

model = LinearRegression()
model.fit(x, y)

print(model.predict([[40]]))
