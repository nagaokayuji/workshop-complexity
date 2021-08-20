# 発展


[Q2-1] 次のコードの計算量は？ 

```python
sum = 0
for i in range(1,N+1): # 1 ~ N まで
  for j in range(i,N+1, i): # N 以下の i の倍数
    sum += 1 # 何かの処理

print(sum)
```

- 外側のループはN回
- 内側のループは各 i によって回数が変わる
    - i=1 のとき、j は 1 ~ N までの **N 通り**
    - i=2 のとき、j は 2, 4, ..., (Nを超えない最大の2の倍数) の個数 ＝ **floor(N/2) 通り**
    - i=3 のとき、j は 3, 6, ..., (Nを超えない最大の3の倍数) の個数 ＝ **floor(N/3) 通り**
    - ...
    - i=N のとき j は N のみとなり、**1 通り**

全部足していくと、$\sum_{i=1}^N \lfloor \frac{N}{i} \rfloor$

最大でどのくらいになるのかを知りたいので、床関数を外して計算していきます。

$$\sum_{i=1}^N \frac{N}{i}  = N \sum_{i=1}^N \frac{1}{i}$$

について近似的に

$$N\int_1^N \frac{1}{x}dx$$

として計算すると

$$O(N \log N)$$

となります。

[参考]

Nを横軸としてプロットした結果 (`plot_harmonic_number.py`)

![https://res.cloudinary.com/ddaz9etkx/image/upload/v1628390160/ot/Figure_1_xppdtp.png](https://res.cloudinary.com/ddaz9etkx/image/upload/v1628390160/ot/Figure_1_xppdtp.png)

関連するアルゴリズム:

- エラトステネスの篩 O(N log log N)
