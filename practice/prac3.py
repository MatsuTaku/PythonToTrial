'''
    文字列が渡されます．
    1文字目から始まり，３文字おきに順に文字を読み出し，新たな文字列を作って返して下さい．
    オフセットが文字列長をはみ出した場合，はみ出した分を新たなオフセットとして下さい．
    引数の文字列長と，変値の文字列長は等しくなります．
    e.g.
         13524
        'acebd' -> 'abcde'
    ※ 入力文字列の長さは，必ず３で割り切れない長さになっています．

    関数名: newSortString
    引数: str
    返値: str
'''
def newSortString(str):
    new = ''
    l = len(str)
    for i in range(l):
        # 文字列長で割った余りを添字にすれば，端数が折り返される
        new += str[i * 3 % l]
    return new




# for DEBUG: -

# 並び替え前文字列の生成
def reverse(text):
    # 3で割り切れないように調整
    if len(text) % 3 == 0:
        text += '_'
    l = len(text)
    new = ' ' * l
    new_list = list(new)
    for i in range(l):
        new_list[i * 3 % l] = text[i]
    return ''.join(new_list)

if __name__ == '__main__':
    rev = reverse('The_Zen_of_Python,_by_Tim_Peters.')
    print(rev)
    print(newSortString(rev))
