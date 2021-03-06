# 計算量の表し方

計算機科学では **ランダウ記法（ビッグオー記法）** と呼ばれるものが一般的に用いられ、**漸近的に上から抑える**ことで計算量を評価します。

※ 後ほど少し触れますが、他にも$\Theta$記法や$\Omega$記法といった表し方もあります。

アルゴリズムへの入力サイズを $N$ としたとき、記号Oを用いて

$O(N)$, $O(N^2)$ のように記します。

また、あるアルゴリズムの計算量が $O(1)$ だとすると、入力サイズによらず常に一定の時間で処理が完了することが期待できます。

O記法では定数倍や増分が少ない項を無視して考えることができ、

$f(x) = 2x^3 + 10x^2 + 20$ は $O(x^3)$ と表されます。

（最も発散速度の速いもので決定される）

## 簡単にオーダー記法にしたい！

式が分かっているとき、一般的に次の手順で求められます。
1. 係数を省略する
2. $N$ が大きいときに最も影響が大きい項のみ取り出す

$f(x) = 2x^3 + 10x^2 + 20$ の例では

1.の手順で $x^3 + x^2 + 1$ となり、さらに2.の手順で$x^3$ が得られます。


## 大きさの比較

大まかには次のようになります。

$O(1) < O(\log N) < O(N) < O(N \log N) < O(N^2) << O(2^N) << O(N!)$ 

時間計算量の場合、$O(1)$ では一瞬で計算可能であり、$O(N^2)$ では時間がかかります。

## [補足] 厳密な定義

ランダウの$O$記法の定義について述べます。

$N$を $0$ 以上の整数とし、関数  $T(N), P(N)$  を定義します。

このとき、「 $T(N) = O(P(N))$ である 」とは、

$$ {}^\exists c, {}^\exists N_0\ge0 \hspace{7px} s.t. \hspace{7px} {}^\forall N [  N_0 \le N \implies |\frac{T(N)}{P(N)}| \le c ]$$

が成り立つことをいいます。

$f(x) = 2x^3 + 10x^2 + 20$ の例では

$$\lim_{x \rightarrow \infty} \frac{f(x)}{x^3}=\lim_{x \rightarrow \infty} \frac{2x^3 + 10x^2 + 20}{x^3} = 2$$

より、 十分大きな $x$ について $|\frac{f(x)}{x^3}| <= c$ ($c$は適当な定数)  となることが示せました。

よって、$f(x) = O(x^3)$  であると言えます。

[注]

この定義では $f(x) = O(x^4)$ や $f(x) = O(x^5)$ などでも成立することがわかります。しかし、通常は$f(x)$の増加速度を最も忠実に表すものを採用し、$O(x^2)$ を用います。
