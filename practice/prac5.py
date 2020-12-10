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

'''
    素数かどうかの真偽値を返す関数
    is~ は，Bool値を返す関数でよく使う命名方法
'''
def isPrime(num):
    '''
        以下は効率のいいアルゴリズムの例
        単純でも出力が正しければ no problem
    '''
    # １以下を足切り
    if num <= 1:
        return False
    # ２以降の偶数を足切り
    # 偶奇の足切りは単純に効率が良い
    if num > 2 and num % 2 == 0:
        return False
    # 探索は，√num までで十分
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    # 全てのフィルタリングを通過すれば，素数である
    return True

def sortedPrimeNumbers(list):
    new = []
    prev = 0 # 重複判定用．素数じゃない値で初期化
    # ソートしてから探索
    for v in sorted(list):
        '''
            途中でcontinueさせるのは，ネストを浅く保つテクニック
        '''
        # 直前と同じものはスキップ
        if v == prev:
            continue
        prev = v
        # 素数判定
        if not isPrime(v):
            continue
        # 追加
        new.append(v)
    return new



# for DEBUG: - 

# フィボナッチ数列
def phibo():
    l = [0, 1]
    for i in range(2, 30):
        v = l[i - 2] + l[i - 1]
        l.append(v)
        i += 1
    print(l)

# ランダム生成
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
