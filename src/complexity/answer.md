# 計算量クイズの解答

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

## Q3-4

元の実装では以下のように何度も同じ処理が呼ばれていました。

![image](https://res.cloudinary.com/ddaz9etkx/image/upload/v1629479070/202108/workshop-figures_oswkqh.png)

![image](https://res.cloudinary.com/ddaz9etkx/image/upload/v1629479371/202108/workshop-figures_1_up2ame.png)

色を付けた部分が同じ引数で呼び出されたものです。
これを削減できれば計算量が改善できそうです。
### $O(N)$ の解法

メモ化再帰 や 動的計画法(Dynamic Programming, DP) と呼ばれる手法を用いて計算すると$O(N)$となります。
#### メモ化再帰

同じ処理が何度も呼ばれるのは無駄ですね。

では、一度計算した内容は保持しておくようにしたらどうでしょうか。

同じ計算は結果がわかっていれば使い回せそうです。

![figure](https://res.cloudinary.com/ddaz9etkx/image/upload/v1629480178/202108/workshop-figures_2_anl0ep.png)


同様に、$F(N-3), F(N-4), \cdots $ も一度だけ計算されるようにした場合、$O(N)$になりそうですね。

これを実現するコードが以下です。

```python
memo = [1] * (N+1) #計算結果のメモ用に、長さ(N+1)のリストを用意
calculated = [False] * (N+1)  #計算済みフラグ
calculated[1] = calculated[2] = True # 1, 2 の場合は1固定のため

def fib(N: int):
    if calculated[N]:   # 一度計算されていたら
        return memo[N]  # memo の内容を返す
    else:
        memo[N] = fib(N-1) + fib(N-2) # 計算されていない場合は計算する
        calculated[N] = True          # 計算済みフラグをTrueにする
        return memo[N]

print(fib(N))
```
わかりやすさのため`calculated`と`memo`に分けていますが、一般的には `memo` のみを使用して実装します。


### DP による解法

再帰を用いず、普通に計算結果を使い回して計算することでも$O(N)$になります。

次の図のようなイメージで、前から計算していきます。

![image](https://res.cloudinary.com/ddaz9etkx/image/upload/v1629481671/202108/workshop-figures_3_uvccuu.png)

```python
def fib(N: int):
    dp = [1] * (N+1) # 第1項、第2項が 1 のため 1 で初期化
    for i in range(3,N+1):  # 普通に前から計算していく
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

print(fib(N))
```

やっていることはメモ化再帰と同様で、**全く同じ処理は繰り返さない** ことがカギとなります。


### $O(\log N)$ の解法

少し高度な内容を含みます。

$$
\begin{pmatrix}
F(N+1) \\
F(N)
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}
\begin{pmatrix}
F(N) \\
F(N-1)
\end{pmatrix}
$$

が成り立つことを利用します。
（これに限らず、漸化式は行列の積で表せることが多いです！）

これより、

$$
\begin{pmatrix}
F(N+1) \\
F(N)
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}^{N-1}
\begin{pmatrix}
F(2) \\
F(1)
\end{pmatrix}
$$
となります。

この計算の計算量を見積もります。

まず、$2 \times 2$ 行列の掛け算は 8 回の掛け算と 4 回の足し算で済むので、定数オーダーです。

また、一般に$A^{2N} = (A^N)^2$ であるため、$A^N$ の計算は$O(\log N)$ であることがわかります。[^1]  
- 例: $2^{10} = 2^{8+2} = (2^2)^4 * 2^2 = ((2^2)^2)^2 * 2^2$ とすると、6回の掛け算で計算できる。

以上より、次のような実装で$O(\log N)$を達成できます。

```python
import numpy as np
def pow(A, n):
    '''
    繰り返し二乗法
    Aは行列
    '''
    ret = np.eye(len(A), dtype=np.int64) # Aと同じサイズの単位行列で初期化
    while n:                             # n > 0 の間
        if n % 2:                        # 最下位のbitが立っている場合
            ret = ret.dot(A)             # 返り値に A を加える
        A = A.dot(A)                     # A に A^2 を代入
        n >>= 1                          # 右シフト
    return ret

def fib(N):
    A = np.array([[1, 1], [1, 0]], dtype=np.int64) # 行列を定義
    mat = pow(A, N-1)                              # 行列の累乗を計算 O(log N)
    ret = mat.dot(np.array([[1], [1]], dtype=np.int64))
    return ret[1][0]
```
上記コードでは `numpy`というライブラリを使用しており、これは数値計算を簡単にするものです。
例えば `A.dot(B)` とすると $A \times B$ の行列積を計算できます。






[^1]: 繰り返し二乗法などと呼ばれます。


## Q3-5

これは **二分探索** という有名なアルゴリズムであり、$O(\log N)$となります。

一回の質問ごとに、答えの範囲が半分以下に絞られるので、試行回数を$M$として式にすると遅くとも $(\frac{1}{2})^M$ の速度で解の存在範囲が小さくなっていきます。


よって、 $N \times (\frac{1}{2})^M = 1$ のときには必ず答えが決まっていることになり、これを$M$について解くと$ M = \log_2 N$ が得られます。

以上より、最悪計算量は$O(\log N)$です。
