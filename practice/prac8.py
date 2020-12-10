'''
    マサオくんとカズヒロくんがじゃんけんをします．
    じゃんけんの手には，
    ✊: 0, ✌(ﾁｮｷ): 1, ✋: 2
    の整数を割り当てます．
    じゃんけんの結果によって以下の数字を返す関数を定義して下さい．
    マサオくんの勝利: 1,
    カズヒロくんの勝利: -1,
    あいこ: 0

    引数は整数値２つです．
    １つ目の引数はマサオくんの手
    ２つ目の引数はカズヒロくんの手
    です．

    関数名: rps
    引数: int, int
    返値: int
'''
def rps(masao, kazuhiro):



# for DEBUG: - 

def generate():
    import random
    for _ in range(15):
        list = [random.randint(0, 2) for _ in range(2)]
        print(list, rps(list[0], list[1]))

if __name__ == '__main__':
    print(rps(2, 0))
    print(rps(2, 1))
    print(rps(2, 2))
    generate()
