N = 100

memo = [1] * (N+1)
calculated = [False] * (N+1)
calculated[1] = calculated[2] = True
def fib(N: int):
    if calculated[N]:
        return memo[N]
    else:
        memo[N] = fib(N-1) + fib(N-2)
        calculated[N] = True
        return memo[N]

print(fib(N))
