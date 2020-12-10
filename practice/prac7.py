'''
    男性グループと女性グループがあります．
    それぞれのグループで，気に入った異性の名前が保存された辞書が作られます．
    男女がお互いに気に入っていた場合，カップルが成立します．
    辞書を元に，成立したカップル数を返す関数を定義して下さい．

    ２つの辞書が渡されます．
    １つ目の辞書は，男性の名前をキーとして，好みの女性の名前を保存しています．
    ２つ目の辞書は，女性の名前をキーとして，好みの男性の名前を保存しています．

    e.g.
        $ num of couples = 1 $
        men: {'Romeo': 'Juliet'}
        women: {'Juliet': 'Romeo'}

        $ num of couples = 0 $
        men: {'Kirito': 'Asuna'}
        women: {
            'Lisabet': 'Kirito',
            'Shirika': 'Kirito',
            'Liifa': 'Kirito',
            'Shinon': 'Kirito',
        }

    関数名: matching
    引数: dict, dict
    返値: int
'''
def matchings(mend, womend):
    count = 0
    # 全ての男性において，好みの女性が自分を好きかどうかが分かれば十分
    for mname in mend.keys():
        '''
            dict.get(key)
            存在するかわからないkeyで辞書からvalueを取り出す関数
            なければ None
        '''
        if mname == womend.get(mend[mname]):
            count += 1
    return count

# for DEBUG: - 

if __name__ == '__main__':
    mdi = {'a': 1, 'b': 2, 'c': 3}
    wdi = {1: 'a', 2: 'b', 3: 'c'}
    print(matchings(mdi, wdi))
