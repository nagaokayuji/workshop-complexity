# 解答
- 外側のループはN回
- 内側のループは各 i によって回数が変わる
    - i=1 のとき、j は 1 ~ N までの **N 通り**
    - i=2 のとき、j は 2, 4, ..., (Nを超えない最大の2の倍数) の個数 ＝ **floor(N/2) 通り**
    - i=3 のとき、j は 3, 6, ..., (Nを超えない最大の3の倍数) の個数 ＝ **floor(N/3) 通り**
    - ...
    - i=N のとき j は N のみとなり、**1 通り**

全部足していくと、$\sum_{i=1}^N \lfloor \frac{N}{i} \rfloor$

床関数を外して計算すると
$$\lfloor\sum_{i=1}^N \frac{N}{i}\rfloor \le \sum_{i=1}^N \frac{N}{i}  = N \sum_{i=1}^N \frac{1}{i}$$

となります。

ここで、
$\sum_{i=1}^N \frac{1}{i}$について

$$
\int_1^{N+1} \frac{1}{x} dx = \log(N+1) \le \sum_{i=1}^N \frac{1}{i} \tag{1}
$$

$$
(\sum_{i=1}^N \frac{1}{i}) - 1= \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{N} \le \int_1^{N} \frac{1}{x} dx =  \log N \tag{2}
$$

が成り立つため、
$(1), (2)$ より
$$
\log (N+1) \le \sum_{i=1}^N \frac{1}{i} \le 1 + \log N \tag{3}
$$
が成り立ちます。

$N > 0$ であるから、
$$
N\log (N+1) \le N\sum_{i=1}^N \frac{1}{i} \le N (1 + \log N)
$$


よって、計算量は


$$O(N \log N)$$

となります。


また、下からも抑えられているため
$$
\Omega (N \log N)
$$
が言えます。


[参考]

Nを横軸としてプロットした結果 (`plot_harmonic_number.py`)

![https://res.cloudinary.com/ddaz9etkx/image/upload/v1628390160/ot/Figure_1_xppdtp.png](https://res.cloudinary.com/ddaz9etkx/image/upload/v1628390160/ot/Figure_1_xppdtp.png)

## $(3)$ の式が成り立つことを確認してみましょう！

```python
import math
N = 10**6

h = 0
for i in range(1, N+1):
    h += 1/i

print("log(N+1) =", math.log(N+1))
print("Hn =", h)
print("1 + log(N) =", 1 + math.log(N))

assert math.log(N+1) <= h <= 1 + math.log(N)
```

関連するアルゴリズム:

- エラトステネスの篩 O(N log log N)