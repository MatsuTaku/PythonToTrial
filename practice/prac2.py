'''
    複数の文字列を要素に持つリストが渡されます．
    リスト内の文字列をスペース(' ')で連結し，１つの文字列を返す関数を定義して下さい．

    関数名: joinStrings
    引数: [str, ...]
    返値: str
'''
def joinStrings(list):
    '''
        str.join(list)
        引数のリストを，自身の文字列で連結した文字列を返す，str型の標準関数
    '''
    return ' '.join(list)

# ループでやるとこんな感じ
def joinStrings2(list):
    joined = ''
    for str in list:
        joined += str + ' '
    return joined[:-1]

# for DEBUG: - 

if __name__ == '__main__':
    print(joinStrings(['py', 'th', 'on', '3']))
