# 練習問題


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