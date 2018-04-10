'''
    整数値のリストが渡されます．
    以下の要素を含む辞書を返す関数を定義して下さい．
    {
       'sum': <リストの合計値>,
       'average': <リストの平均値>,
       'median': <リストの中央値>,
     }
    ※ リストの平均値は，float型のままで大丈夫です．

    関数名: getStatistics
    引数: [int, ...]
    返値: {str: int, str: float, str: int}
'''
def getStatistics(list):
    res = {}
    res['sum'] = sum(list)
    res['average'] = res['sum'] / len(list)
    res['median'] = sorted(list)[len(list) // 2]
    return res

if __name__ == '__main__':
    print(getStatistics([1,2,3,4,5,6,8]))
    print(getStatistics([6,2,6,8,4,2,5,2,6]))
