import numpy as np
from timeit import timeit


def main():
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
    n = 10000
    print(timeit(lambda: np.matmul(a, b), number=n) / n * 10**9)

    print("Multiply two 100000 element numpy arrays")
    a = np.arange(10000).reshape(100, 100)
    b = np.arange(10000).reshape(100, 100)
    n = 10
    print(timeit(lambda: np.matmul(a, b), number=n) / n * 10**9)


if __name__ == '__main__':
    main()
