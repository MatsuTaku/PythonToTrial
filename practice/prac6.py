'''
    整数値のリストが渡されます．
    以下の要素を含む辞書を返す関数を定義して下さい．
    {
       'sum': <リストの合計値>,
       'average': <リストの平均値>,
       'median': <リストの中央値>,
     }
    ※ リストの平均値は，float型のままで大丈夫です．
    ※ 中央値の定義:
        リスト長が奇数の場合，整列済みリストの真ん中の値
        リスト長が偶数の場合，整列済みリストの真ん中二つの値の平均値
    ※ 中央値，floatにしてね！

    関数名: getStatistics
    引数: [int, ...]
    返値: {str: int, str: float, str: float}
'''
# リストの中央値出す関数
def median(list):
    sl = sorted(list)
    l = len(sl)
    if l % 2 == 0:
        return (sl[l // 2] + sl[l // 2 - 1]) / 2
    else:
        return float(sl[l // 2])

def getStatistics(list):
    stat = {}
    '''
        sum(list)
        リストの内部数値の合計値を出す標準関数
        len(list)
        リスト長を出す標準関数
    '''
    stat['sum'] = sum(list)
    stat['average'] = stat['sum'] / len(list)
    stat['median'] = median(list)
    return stat

# for DEBUG: - 

if __name__ == '__main__':
    print(getStatistics([1,2,3,4,5,6,8]))
    print(getStatistics([6,2,6,8,4,2,5,2,6]))
