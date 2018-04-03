'''
    整数値のリストが渡されます．
    リストに含まれる素数のみで，新たに配列を作って下さい．
    重複した値は除去して下さい．
    昇順にソートして下さい．
    出来た配列を返す関数を定義して下さい．
    Advice.
        受け取った値が素数であるかどうかを判断する関数を作ると，処理が綺麗になります．
        条件を満たすように，柔軟にコーディングしてみましょう．

    関数名: sortedPrimeNumbers
    引数: [int, ...]
    返値: [int, ...]
'''
import math

def isPrime(num):
    if num <= 0:
        return False
    if num > 2 and num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def sortedPrimeNumbers(list):
    new = []
    for v in list:
        if not isPrime(v) or v in new:
            continue
        new.append(v)
    return sorted(new)

def phibo():
    l = [0, 1]
    for i in range(2, 30):
        v = l[i - 2] + l[i - 1]
        l.append(v)
        i += 1
    print(l)

def rand(size):
    import random
    l = []
    for _ in range(30):
        l.append(random.randint(1, size))
    print(l)

if __name__ == '__main__':
    list = [x % 30 + 1 for x in range(90, 1, -1)]
    print(list)
    print(sortedPrimeNumbers(list))
    print([x for x in range(30, 0, -1)])
    phibo()
    rand(100)
    rand(200)
    rand(300)
    rand(400)
    rand(500)
