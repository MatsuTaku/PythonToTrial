# Python 学習プログラム
第一回勉強会の課題です．  
全８問をPythonで実装し，採点プログラムで採点してみましょう．

## 環境
- Python(Python3) コマンドが実行可能なPC
  - WindowsPCへのPython環境のインストールは，こちらを参照して下さい  
    [Pythonをインストールする（for Windows） - Qiita](https://qiita.com/taiponrock/items/f574dd2cddf8851fb02c)

## コマンドプロンプト(CMD)
WindowsのCLIです．本プログラムは，こちらのCLI上での実行を想定しています．

### 起動方法
1. __Windows システムツール -> コマンド プロンプト__

### ディレクトリの移動
```
$ cd [directory_path]
```
ディレクトリパスは，ファイルエクスプローラからディレクトリをCMDにドラッグ＆ドロップで記述できます．

## プログラミングのすすめ
問題単位で実行しながらプログラミングをすると，デバッグしやすいですね．  
以下のように実行時処理を書きながら作業すると，捗ると思います．
```prac1.py
...
def getLangName():
  # 問題の処理

if __name__ == '__main__':
  text = getLangName()
  print(text)
```
CMDで以下のように実行します．
```
$ python prac1.py
> Python3
```

## 採点プログラムの使い方
1. __prac[number].py__ の問題を解く
2. コマンドプロンプト(CMD)上で，問題のあるディレクトリに移動
3. 採点プログラムを実行
```
$ python judge.py [number]
```
4. 各caseについて正誤判定が行われる
```
例
$ python judge.py 3
case 1 : accept
case 2 : accept
case 3 : accept
case 4 : accept
case 5 : accept
case 6 : accept
Clear!
```
