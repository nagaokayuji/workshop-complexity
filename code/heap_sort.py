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


def heap_sort(l: list):
    heap = MinHeap()
    for value in l:
        heap.push(value)
    ret = []
    while not heap.is_empty():
        ret.append(heap.pop())
    return ret


l = [12, 1, 4, 5, 1, -3, 2, 234, 2]

print(heap_sort(l))
