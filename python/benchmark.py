import numpy as np
from timeit import timeit


def old_style():
    print("Benchmarking NumPy")

    print("Add two 100 element numpy arrays")
    a = np.arange(100)
    b = np.arange(100)
    n = 1000000
    print(timeit(lambda: a + b, number=n) / n * 10**9)

    print("Add two 100000 element numpy arrays")
    a = np.arange(100000)
    b = np.arange(100000)
    n = 10000
    print(timeit(lambda: a + b, number=n) / n * 10**9)

    print("Multiply two 10x10 element numpy arrays")
    a = np.arange(100).reshape(10, 10)
    b = np.arange(100).reshape(10, 10)
    n = 100000
    print(timeit(lambda: np.matmul(a, b), number=n) / n * 10**9)

    print("Multiply two 100x100 element numpy arrays")
    a = np.arange(10000).reshape(100, 100)
    b = np.arange(10000).reshape(100, 100)
    n = 1000
    print(timeit(lambda: np.matmul(a, b), number=n) / n * 10**9)

    print("Transpose a 10x10 matrix")
    a = np.arange(100).reshape(10, 10)
    n = 10000
    print(timeit(lambda: np.transpose(a), number=n) / n * 10**9)

    print("Transpose a 100x100 matrix")
    a = np.arange(10000).reshape(100, 100)
    n = 10
    print(timeit(lambda: np.transpose(a), number=n) / n * 10**9)


def new_style():
    trials = 30
    np.set_printoptions(suppress=True)

    a = np.arange(100000).astype('float32')
    b = np.arange(100000).astype('float32')
    c = a + b
    data = np.zeros(trials).astype(int)
    for i in range(trials):
        data[i] = round(timeit(lambda: a + b, number=1) * 10 ** 9)

    print(data)

    a = np.arange(10000).reshape(100, 100).astype('float32')
    b = np.arange(10000).reshape(100, 100).astype('float32')
    c = np.matmul(a, b)
    data = np.zeros(trials).astype(int)
    for i in range(trials):
        data[i] = round(timeit(lambda: np.matmul(a, b), number=1) * 10 ** 9)

    print(data)

    a = np.arange(10000).reshape(100, 100).astype('float32')
    c = np.transpose(a)
    data = np.zeros(trials).astype(int)
    for i in range(trials):
        data[i] = round(timeit(lambda: np.transpose(a), number=1) * 10 ** 9)

    print(data)


def main():
    new_style()


if __name__ == '__main__':
    main()
