import math

N = 10**6

h = 0
for i in range(1, N+1):
    h += 1/i

print("log(N+1) =", math.log(N+1))
print("Hn =", h)
print("1 + log(N) =", 1 + math.log(N))


assert math.log(N+1) <= h <= 1 + math.log(N)
