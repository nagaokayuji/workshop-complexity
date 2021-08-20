import numpy as np


def pow(A, n):
    '''
    繰り返し二乗法
    Aは行列
    '''
    ret = np.eye(len(A), dtype=np.int64)
    while n:
        if n % 2:
            ret = ret.dot(A)
        A = A.dot(A)
        n >>= 1
    return ret


def fib(N: np.int64):
    A = np.array([[1, 1], [1, 0]], dtype=np.int64)
    mat = pow(A, N-1)
    ret = mat.dot(np.array([[1], [1]], dtype=np.int64))
    return ret[1][0]


print(fib(10))
