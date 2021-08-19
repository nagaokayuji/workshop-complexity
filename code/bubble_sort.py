def bubble_sort(l: list):
    n = len(l)
    print(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        print(l)
    return l
