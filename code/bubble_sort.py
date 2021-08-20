def bubble_sort(a: list):
    n = len(a)
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i] # スワップ
    return a

l = [128,6,1,22,2,-12,34,293,208,14,7,67,-123,5,166,43]

print(bubble_sort(l))