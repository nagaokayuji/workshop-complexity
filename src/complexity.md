# 計算量とはなにか

## 計算量(computational complexity)とは

結果が同じ処理でも、使用するアルゴリズムによって実行時間が変わることがあります。

その計算コストを評価するために用いるものが計算量です。

尺度によって以下の定義があります。

- 時間計算量
    - 計算のステップ数
- 空間計算量
    - 記憶領域の使用量

以下は**時間計算量**についての内容となります。

## 計算量の表し方

計算機科学では **ランダウ記法（ビッグオー記法）** と呼ばれるものが一般的に用いられ、**漸近的に上から抑える**ことで計算量を評価します。

※ 後ほど少し触れますが、他にも$\Theta$記法や$\Omega$記法といった表し方もあります。

アルゴリズムへの入力サイズを $N$ としたとき、記号Oを用いて

$O(N)$, $O(N^2)$ のように記します。

また、あるアルゴリズムの計算量が $O(1)$ だとすると、入力サイズによらず常に一定の時間で処理が完了することが期待できます。

O記法では定数倍や増分が少ない項を無視して考えることができ、

$f(x) = 2x^3 + 10x^2 + 20$ は $O(x^3)$ と表されます。

（最も発散速度の速いもので決定される）

### [補足] 厳密な定義

ランダウの$O$記法の定義について述べます。

$N$を $0$ 以上の整数とし、関数  $T(N), P(N)$  を定義します。

このとき、「 $T(N) = O(P(N))$ である 」とは、

$$ {}^\exists c, {}^\exists N_0\ge0 \hspace{7px} s.t. \hspace{7px} {}^\forall N [  N_0 \le N \implies |\frac{T(N)}{P(N)}| \le c ]$$

が成り立つことをいいます。

$f(x) = 2x^3 + 10x^2 + 20$ の例では

$$\lim_{x \rightarrow \infty} \frac{f(x)}{x^3}=\lim_{x \rightarrow \infty} \frac{2x^3 + 10x^2 + 20}{x^3} = 2$$

より、 十分大きな $x$ について $|\frac{f(x)}{x^3}| <= 3$  となることが示せます。

よって、$f(x) = O(x^3)$  であると言えます。

[注]

この定義では $f(x) = O(x^4)$ や $f(x) = O(x^5)$ などでも成立することがわかります。しかし、通常は$f(x)$の増加速度を最も忠実に表すものを採用し、$O(x^2)$ を用います。

## 処理時間について

**1秒あたり $10^8$ ステップ**の演算が可能であると仮定します。（一般的なCPUのクロック周波数は 1 ~ 5 GHz程度、1ステップあたり10クロック程度）

このとき、およそ$10^8$ステップにつき1秒の時間がかかることになります。

このことから、

数万件のデータに対して$O(N^2)$のアルゴリズムで処理すると、数秒で終了することが期待できます。

しかし、数十万件のデータに対して同様の処理を実行した場合、数百秒程度の実行時間となってしまいます。（実際にはさらにかかる場合が多い）

一方、同様の結果が得られる処理を$O(N \log N)$のアルゴリズムで構築した場合、数百万件のデータに対しても**数ミリ秒**で処理を完了することができます。

※このような数百万件のデータは実世界でも多く現れ、また$O(N^2)$の処理を$O(N\log N)$にすることで高速化できる処理は多くあります。

→ SQL のJOINなど


### ソートの計算量

プログラミングの本などでよく出てくるソートアルゴリズムの計算量は以下のようになっています。

計算量表記はは最悪ケースの時間計算量です。

- [可視化された動画](https://youtu.be/ZZuD6iUe3Pc)

####  バブルソート: $O(N^2)$

順序通りになっていない2要素に対して swap を繰り返していけばいつかは
ソートされるだろう、というアルゴリズムです。

ライブラリや他のアルゴリズムを知らない状態でソートを実装しろと言われたら、誰もがこの方法で実装するのではないでしょうか。

関連: 転倒数

実装例は以下です。
簡単のため常に$O(N^2)$の計算量となりますが、
ソートされていたら終了、という処理を追加すると最良で$O(N)$となります。

```python
def bubble_sort(l: list):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
```


####  ヒープソート: $O(N \log N)$

ヒープと呼ばれるデータ構造にすべてのデータを突っ込み、全部取り出すとソートされます。

- 最小ヒープの例
  - 二分木で格納
  - どのノードにおいても 親ノード < 子ノード となるようにする
  - 根が最小値となる


シンプルなヒープの実装は以下のようになります。

```python
class MinHeap:
    def __init__(self):
        self.array = []

    def push(self, value):
        n = len(self.array)
        self.array.append(value)
        while n:  # n が 0 より大きい場合
            # 二分木上で親の index は以下のようになる
            parent = (n-1)//2
            if self.array[n] < self.array[parent]:  # swap
                self.array[n], self.array[parent] = self.array[parent], self.array[n]
            n = parent

    def pop(self):
        value = self.array[0]  # 取り出す値(最小値)
        self.array[0] = self.array[-1]  # 最後の要素を一時的に根にする
        self.array.pop()  # 最後の要素を削除
        n = len(self.array)
        i = 0
        while 2*i+1 < n:
            j = 2*i+1
            # 子のうち小さい方の index を j にする
            if j+1 < n and self.array[j] > self.array[j+1]:
                j += 1
            # 親 < 子になるように swap
            if self.array[i] > self.array[j]:
                self.array[i], self.array[j] = self.array[j], self.array[i]
            i = j
        return value

    def is_empty(self):
        return len(self.array) == 0
```

これを用いて、以下のようにソートを実装できます。

```python
def heap_sort(l: list):
    heap = MinHeap()
    for value in l:
        heap.push(value)
    ret = []
    while not heap.is_empty():
        ret.append(heap.pop())
    return ret
```

#### マージソート: $O(N \log N)$

フォン・ノイマン 考案のアルゴリズムです。

**分割統治法** と呼ばれる手法でソートします。

データ数が1や2のデータに対しては簡単にソートできることを利用し、
二等分したデータに対して再帰的に処理します。マージする際は小さい方から順にとっていく形になります。

```python
def merge_sort(l: list):
    n = len(l)
    if n <= 1:
        return l

    # a, b に分割
    # 分割したa, bに対して sort
    a = merge_sort(l[0:n//2])
    b = merge_sort(l[n//2:])

    # マージ処理
    index_a = index_b = 0
    ret = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            ret.append(a[index_a])
            index_a += 1
        else:
            ret.append(b[index_b])
            index_b += 1
    # 余った要素を最後に追加
    if index_a < len(a):
        ret += a[index_a:]
    else:
        ret += b[index_b:]
    return ret
```


#### クイックソート: $O(N^2)$

こちらも分割統治法の一種です。

代表的なアルゴリズムの中では最も高速とされています。

最悪計算量$O(N^2)$ですが、平均では$O(N \log N)$となります。

適当にピボットと呼ばれる値を決め、その値をしきい値として分割していき、順にマージしていきます。

シンプルに実装すると以下のようになりますが、一般的な実装よりパフォーマンスが悪いです。

```python
def quick_sort(l: list):
    if len(l) <= 1:
        return l
    pivot = l[0] # 適当に選ぶ
    a = list(filter(lambda x: x < pivot, l))
    b = list(filter(lambda x: x == pivot, l))
    c = list(filter(lambda x: x > pivot, l))
    return quick_sort(a) + b + quick_sort(c)
```


### ちなみに・・・

ソート処理の最悪計算量は最高でも$O(N\log N)$であることが数学的に示されています。

- アルゴリズムを二分決定木として表し、ノード＝比較処理、その結果に応じた処理を辺に対応付ける。
- 二分決定木の高さを$m$としたとき、$m$は最悪計算量に対応し、ノード数は$2^m$ 以下となる。
- しかし、任意の入力に対応した二分決定木を作るためには、ノードが $N!$ **個以上**存在する必要がある。
- よって $N! \le 2^m$ **が必要** となり、 $m = \Omega(N \log N)$となる。

※ $O$記法は上から評価するのに対し、$\Omega$記法は下から評価するものです。

よって、$\Omega(N \log N)$は最低でも$N \log N$ステップ必要であることを意味しており、クイックソートの最悪計算量$O(N \log N)$は漸近的に最適であると言えます。

### 例題

以下、$N$, $M$ は定数とします。

[Q1-1]

```python
sum = 0
for i in range(N): # 0 ~ N-1 まで繰り返し
  sum += 1 # 何かの処理

for i in range(N): # 0 ~ N-1 まで繰り返し
  sum += 1

print(sum)
```

[答え]

$N + N = 2N$ 回のループとなります。

定数倍は無視できるため、全体の計算量は $O(N)$ です。

[Q1-2] 

```python
sum = 0
for i in range(1, N + 1): # 1 ~ N まで繰り返し
  for j in range(1, N + 1): # 1 ~ N まで繰り返し
    sum += 1

print(sum)
```

[答え]

$N \times N = N^2$ 回のループとなります。

この場合の計算量は $O(N^2)$ です。

[Q1-3]

```python
sum = 0
for i in range(1, N): # 1 ~ N-1 まで繰り返し
  for j in range(i+1, N): # i+1 ~ N-1 まで繰り返し
    sum += 1

print(sum)
```

[答え]

ループ回数は $\sum_{i=1}^{N-1}\sum_{j=i+1}^{N-1}1 =\frac{(N-1)(N-2)}{2}$ となります。

低次の項は無視できるため、計算量は $O(N^2)$  です。

[Q1-4]

```python
sum = 0
for i in range(N):
  for j in range(M):
    sum += 1
print(sum)
```

[答え]

$N \times M$ 回のループになります。

全体の計算量としては $O(MN)$ です。

[Q1-5]

```python
sum = 0
i = 1
while i * i <= N:
  i += 1
  sum += 1

print(sum)
```

[答え]

`while` 内の処理の実行回数を考えると、$\lfloor\sqrt{N}\rfloor$ 回となります。

よって、計算量は $O(\sqrt{N})$ です。

### 発展

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

## 練習問題

[Q3-1] 次のコードの計算量は？

```python
sum = 0
while i < N:
  sum += 2

print(sum)
```


[Q3-2] 
次のコードの計算量は？

```python
sum = 0
for i in range(2, N):
    for j in range(i**3, N, i**3):  # i の 3乗
        sum += 1

print(sum)
```

ヒント: `j = i*i*i` の部分が `j = i` だと [Q2-1] になります。

[Q3-3]

次のコードはフィボナッチ数列 {1, 1, 2, 3, 5, 8, 13, 21, ...} の第$N$項を求めるものです。

計算量はどの程度でしょうか？（難しいのでおおよそでOKです） 

また、Nの値がいくつ程度のときに数秒以内で処理が完了できそうでしょうか？

```python
def fib(N: int):
    if N <= 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)

print(fib(N))
```

ヒント:

この関数を$F(N)$とおくと

$$\begin{aligned}f(N)&=f(N-1)+f(N-2) \\ &= \{f(N-2)+f(N-3)\} + \{f(N-3) + f(N-4)\}\\ &= \cdots \end{aligned}$$

[Q3-4] 上記のフィボナッチ数列の第$N$項を求める関数を効率化してみましょう。

[Q3-5] 以下のコードの **最悪計算量** は？


```python
from random import randint
def guess_number(N: int):
    target = randint(0, N)  # 1以上N 以下の適当な数字（整数）を選んでもらう
    sum = 0  # 当てるまでに質問した回数

    # 開始時の範囲は [1, N+1) (半開区間)
    low = 1
    high = N+1
    while True:
        mid = (low + high) // 2  # 中間を選ぶ
        sum += 1
        if mid == target: # 正解したら終了
            return sum
        elif mid < target:
            low = mid
        else:
            high = mid
```

これは次のような数当てゲームに言い換えられます。

- 出題者は `target` となる1以上N以下の整数をランダムに選ぶ。
- 回答者が正解するまで以下を繰り返す。
  - 回答者が適当な数字を選ぶ
  - 不正解の場合、出題者は`target`より大きい・小さい のどちらかで答える

上記のコードは回答者が半分ずつに区間を絞っていくことで正解を探すアルゴリズムです。

## さいごに

計算量はアルゴリズムの良し悪しを測るための重要な指標となるものです。

計算量について知っておくと、実装しようとしているアルゴリズムの実行に要する時間をあらかじめざっくりと見積もることが可能になります。

---

### 参考書籍

大槻 兼資 「問題解決力を鍛える!アルゴリズムとデータ構造」講談社

秋葉 拓哉, 岩田 陽一, 北川 宜稔「プログラミングコンテストチャレンジブック [第2版]」マイナビ出版