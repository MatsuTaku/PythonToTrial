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
        new += str[i * 3 % l]
    return new

def reverse(text):
    if len(text) % 3 == 0:
        text += '_'
    l = len(text)
    new = ' ' * l
    new_list = list(new)
    for i in range(l):
        new_list[i * 3 % l] = text[i]
    return ''.join(new_list)

if __name__ == '__main__':
    print(reverse('The_Zen_of_Python,_by_Tim_Peters.'))
    print(reverse('Beautiful_is_better_than_ugly.'))
    print(reverse('Explicit_is_better_than_implicit.'))
    print(reverse('Simple_is_better_than_complex.'))
    print(reverse('Flat_is_better_than_dense.'))
    print(reverse('Readability_counts.'))
