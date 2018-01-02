from sklearn import linear_model
reg = linear_model.LinearRegression()
X = [[1], [2], [3], [100], [20]]
Y = [1, 2,3,100,20]
reg.fit (X, Y)
print(reg.coef_)