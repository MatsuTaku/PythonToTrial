# Python 学習プログラム
## 使い方
1. __prac[number].py__ の問題を解く
2. `python3 judge.py [number]`を実行
3. 各caseについて正誤判定が行われる．
```例
$ python3 judge.py 3
case 1 : accept
case 2 : accept
case 3 : accept
case 4 : accept
case 5 : accept
case 6 : accept
Clear!
```


## 問題の追加方法
1. 任意の問題ファイルを作成「__prac[number].py__」
```
'''
    問題を説明して下さい．
    関数名:
    引数:
    返値:
'''
# def 関数を定義
```

2. __question.py__ に問題を追加
```
...
import prac[number]
def practice(num):
    ...
    if num == [number]:
        return prac[number].[func]
    ...
```

3. __anspac/judger.py__に，問題で定義した関数の呼び出しを記述
