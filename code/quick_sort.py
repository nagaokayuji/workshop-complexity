
def quick_sort(l: list):
    if len(l) <= 1:
        return l
    pivot = l[0]
    a = list(filter(lambda x: x < pivot, l))
    b = list(filter(lambda x: x == pivot, l))
    c = list(filter(lambda x: x > pivot, l))
    return quick_sort(a) + b + quick_sort(c)


l = [12, 4, -3, 1, 3, -7, 5, 12, -4242, 12, 1234]

print(quick_sort(l))
