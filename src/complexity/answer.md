# 解答

## Q3-1
```python
i = 0
while i < N:
  print(i)
  i += 2
```

$\frac{N}{2}$ 回のループなので、計算量としては $O(N)$ となります。


## Q3-2
```python
sum = 0
for i in range(2, N+1):
    for j in range(i**3, N+1, i**3):  # i の 3乗
        sum += 1

print(sum)
```

まず、外側のループで$N-1$回はかかってしまいます。

内側のループについて考えると、
- $i = 2$ のとき、 $j$ は $\lfloor N/2^3 \rfloor = \lfloor N/8 \rfloor$ 通り
- $i = 3$ のとき、 $j$ は $\lfloor N/3^3 \rfloor = \lfloor N/27 \rfloor$ 通り
- ...
- $i > \sqrt[3]{N}$ のとき、 $j$ は $\lfloor N/i^3\rfloor = $ 0 通り

のようになり、非常に小さい値となることがわかります。

式にすると、
$$
\sum_{i=2}^N \lfloor \frac{N}{i^3} \rfloor
$$
となります。

床関数を外すと、
$$
\sum_{i=2}^N \frac{N}{i^3}   = N \sum_{i=2}^N \frac{1}{i^3}
$$

実は
$$\sum_{i=1}^\infty \frac{1}{i^3} \approx 1.202\cdots$$
となり、収束します。

よって、全体の計算量としては$O(N)$です。

参考: 
- ゼータ関数
- [WolframAlpha](https://ja.wolframalpha.com/input/?i=%CE%B6%283%29)


$N$を変えてプロットすると以下のようになり、計算量が$O(N)$ 以下となることがわかるかと思います。

![figure](https://res.cloudinary.com/ddaz9etkx/image/upload/v1629303914/202108/Figure_1_trhpmj.png)


## Q3-3

```python
def fib(N: int):
    if N <= 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)

print(fib(N))
```


簡単な実装ですが、$N$が大きくなると指数関数的に計算量が爆発してしまいます。

$N > 2$ のとき、 `fib(N)`関数を一回呼ぶごとに`fib(N-1)`と `fib(N-2` が呼ばれていることがわかります。
終了するのは$N$が$2$以下になったときです。

### 雑に見積もる → $O(2^N)$

`fib()`を呼ぶたびに$N$の値が$1$または$2$減っていきますが、このままだと見積もりにくいです。

最後の行が `return fib(N-1) + fib(N-1)` だったらどうでしょうか。

この場合は比較的単純になり`fib(N)` を実行すると`fib(N-1)`が2回呼ばれ、$N$が$2$になるまで繰り返されます。


図にすると以下のようになります。
![image](https://res.cloudinary.com/ddaz9etkx/image/upload/v1629306971/202108/t_vuseqo.png)


このとき、`fib()`関数が呼ばれる回数は $1 + 2 + 4 + \cdots + 2^{N-2}$ となるため、この場合の計算量は$O(2^N)$です。


元の問題を考えると、最後の行で `fib(N-1)`と`fib(N-2)` が呼ばれる場合のほうが計算量が少なくなり、呼び出し回数は$2^N$より小さくなることがわかります。

よって、計算量としては $O(2^N)$ とすることができます。


### 詳しく解析する

$T(N)$を時間計算量の関数とすると、

$T(2) = T(1) = O(1)$ は自明です。

また、$N>2$のとき、加算などの基本的な演算を考慮して

$T(N) = T(N-1) + T(N-2) + O(1)$
が言えます。

これはフィボナッチ数列と同様の増加の仕方となります。

フィボナッチ数列の一般項は
$$
\frac{1}{\sqrt{5}} \left\{ \left( \frac{1+\sqrt{5}}{2} \right)^n - \left( \frac{1-\sqrt{5}}{2} \right)^n \right\}
$$
であるため、計算量としては$O((\frac{1 + \sqrt{5}}{2})^N)$です。