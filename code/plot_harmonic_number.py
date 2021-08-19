import matplotlib.pyplot as plt
import numpy as np


def count_harmonic_numbers(n: int):
    count = 0
    for i in range(1, n+1):  # 1 ~ N まで
        for _ in range(i, n+1, i):  # N以下の i の倍数
            count += 1
    return count


x = np.linspace(1, 10**5, 100, dtype='int')
y = list(map(lambda x: count_harmonic_numbers(x), x))
y2 = x * np.log(x)
print(y)
print(y2)
plt.plot(x, y, label="count")
plt.plot(x, y2, label="NlogN")
plt.plot(x, x, label="N")
plt.legend()
plt.show()
