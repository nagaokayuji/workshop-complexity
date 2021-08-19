import numpy as np
import matplotlib.pyplot as plt
N = 10**7


def count(N):
    sum = 0
    for i in range(2, N+1):
        for j in range(i**3, N+1, i**3):  # i の 3乗
            sum += 1
    return sum


print(sum)


def plot():
    x = np.linspace(1, 10**5, 100, dtype='int')
    y = list(map(lambda x: count(x), x))
    print(y)
    plt.plot(x, y, label="count")
    plt.plot(x, x, label="N")
    plt.legend()
    plt.show()
