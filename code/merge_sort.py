

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


l = [12, 34, 1, 234, 1234, 55, 1, 234, 12, 412, -1124]
print(merge_sort(l))
