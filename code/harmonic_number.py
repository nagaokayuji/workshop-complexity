N = 10**3
count = 0

for i in range(1, N+1):  # 1 ~ N まで
    for j in range(i, N+1, i):  # N以下の i の倍数
        count += 1

print(count)
