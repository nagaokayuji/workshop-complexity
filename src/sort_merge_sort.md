# マージソート: $O(N \log N)$

ノイマン型コンピュータ[^1] の発案者である フォン・ノイマン 考案のアルゴリズムです。

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

[^1]: CPU + 記憶装置 で構成される計算機を指し、現代のコンピュータはほぼ全てノイマン型コンピュータです。

