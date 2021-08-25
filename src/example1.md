# 例題


以下、$N$, $M$ は定数とします。

## [Q1-1]

```python
sum = 0
for i in range(N): # 0 ~ N-1 まで繰り返し
  sum += 1 # 何かの処理

for i in range(N): # 0 ~ N-1 まで繰り返し
  sum += 1

print(sum)
```

### [答え]

$N + N = 2N$ 回のループとなります。

定数倍は無視できるため、全体の計算量は $O(N)$ です。

## [Q1-2] 

```python
sum = 0
for i in range(1, N + 1): # 1 ~ N まで繰り返し
  for j in range(1, N + 1): # 1 ~ N まで繰り返し
    sum += 1

print(sum)
```

### [答え]

$N \times N = N^2$ 回のループとなります。

この場合の計算量は $O(N^2)$ です。

## [Q1-3]

```python
sum = 0
for i in range(1, N): # 1 ~ N-1 まで繰り返し
  for j in range(i+1, N): # i+1 ~ N-1 まで繰り返し
    sum += 1

print(sum)
```

### [答え]

ループ回数は $\sum_{i=1}^{N-1}\sum_{j=i+1}^{N-1}1 =\frac{(N-1)(N-2)}{2}$ となります。

低次の項は無視できるため、計算量は $O(N^2)$  です。

## [Q1-4]

```python
sum = 0
for i in range(N):
  for j in range(M):
    sum += 1
print(sum)
```

### [答え]

$N \times M$ 回のループになります。

全体の計算量としては $O(MN)$ です。

## [Q1-5]

```python
sum = 0
i = 1
while i * i <= N:
  i += 1
  sum += 1

print(sum)
```

### [答え]

`while` 内の処理の実行回数を考えると、$\lfloor\sqrt{N}\rfloor$ 回となります。

よって、計算量は $O(\sqrt{N})$ です。