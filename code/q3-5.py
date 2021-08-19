from random import randint

N = 10000


def guess_number(N: int):
    target = randint(0, N)  # 1以上N 以下の適当な数字（整数）を選んでもらう
    sum = 0  # 当てるまでに質問した回数

    # 開始時の範囲は [1, N+1)  (半開区間)
    low = 1
    high = N+1
    while True:
        mid = (low + high) // 2  # 中間を選ぶ
        sum += 1
        if mid == target:
            return sum
        elif mid < target:
            low = mid
        else:
            high = mid


print(guess_number(11111111))
