# クイックソート: $O(N^2)$

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
