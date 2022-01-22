import numpy as np


def lin_interpolate(data):
    # normal equation for linear regression is
    # theta = ((X_T · X) ^ -1)  · X_T · y
    data = np.array(data)
    X = np.ones_like(data)  # want 2nd col all 1s for intercept term
    X[:, 0] = data[:, 0]    # set first col
    y = data[:, 1]
    inv = np.linalg.inv(np.dot(X.transpose(), X))
    theta = np.dot(inv, np.dot(X.transpose(), y))
    return tuple(theta)


print(lin_interpolate([(1, 2), (3,4), (5,6), (8, 8), (7, -1)]))
