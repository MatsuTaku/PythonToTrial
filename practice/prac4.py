'''
    文字列が渡されます．
    文字列長が 11 未満であれば，True
    11 以上であれば，False
    を返す関数を定義して下さい．

    関数名: shorter11
    引数: str
    返値: bool
'''
def shorter11(str):
    '''
        これを誘うひっかけ問題
        if len(str) < 11:
            return True
        else:
            return False
    '''
    # 比較演算の結果はBool
    return len(str) < 11

# for DEBUG: - 

if __name__ == '__main__':
    print(shorter11('aaaaaaaaaa'))
    print(shorter11('aaaaaaaaaaa'))
