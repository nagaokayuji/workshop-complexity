N = 100


def fib(N: int):
    dp = [1] * (N+1)  # 第1項、第2項が 1 のため 1 で初期化
    for i in range(3, N+1):  # 普通に前から計算していく
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]


print(fib(N))
