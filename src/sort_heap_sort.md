# ヒープソート: $O(N \log N)$

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
    heap = MinHeap() # ヒープを作成
    for value in l:
        heap.push(value) # 全部突っ込む
    ret = []
    while not heap.is_empty():
        ret.append(heap.pop()) # ヒープから全部取り出してリストに入れる
    return ret
```