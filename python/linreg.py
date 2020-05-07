# Source:
# https://towardsdatascience.com/linear-regression-from-scratch-with-numpy-implementation-finally-8e617d8e274c
import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from time import time

# print("Total samples in our dataset is: {}".format(X.shape[0]))


def compute_cost(X, y, params):
    n_samples = len(y)
    h = X @ params
    return (1/(2*n_samples))*np.sum((h-y)**2)


def gradient_descent(X, y, params, learning_rate, n_iters):
    n_samples = len(y)
    J_history = np.zeros((n_iters, 1))

    for i in range(n_iters):
        params = params - (learning_rate/n_samples) * X.T @ (X @ params - y)
        J_history[i] = compute_cost(X, y, params)

    return (J_history, params)


def linreg(X, y):

    n_samples = len(y)

    mu = np.mean(X, 0)
    sigma = np.std(X, 0)

    X = (X-mu) / sigma

    X = np.hstack((np.ones((n_samples, 1)), X))
    n_features = np.size(X, 1)
    params = np.zeros((n_features, 1))

    n_iters = 1500
    learning_rate = 0.01

    initial_cost = compute_cost(X, y, params)

    # print("Initial cost is: ", initial_cost, "\n")

    (J_history, optimal_params) = gradient_descent(
        X, y, params, learning_rate, n_iters)

    # print("Optimal parameters are: \n", optimal_params, "\n")

    # print("Final cost is: ", J_history[-1])

    # plt.plot(range(len(J_history)), J_history, 'r')

    # plt.title("Convergence Graph of Cost Function")
    # plt.xlabel("Number of Iterations")
    # plt.ylabel("Cost")
    # plt.show()


def main():
    dataset = load_boston()

    X = dataset.data
    y = dataset.target[:, np.newaxis]

    times = 31
    tm = [0 for i in range(times)]
    tm[0] = time()
    for i in range(1, times):
        linreg(X, y)
        tm[i] = time()

    for i in range(1, times):
        print((tm[i] - tm[i - 1]) * 10**9)


if __name__ == '__main__':
    main()
