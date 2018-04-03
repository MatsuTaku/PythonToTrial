'''
{'writer': 'Takuma Matsumoto', 'date': '22/3/2018'}
'''

import sys
import anspac
# Import practice scripts...
import prac1
import prac2
import prac3
import prac4
import prac5
import prac6
import prac7
import prac8

def practice(num):
    if num == 1:
        return prac1.showLangName
    if num == 2:
        return prac2.joinStrings
    if num == 3:
        return prac3.newSortString
    if num == 4:
        return prac4.shorter11
    if num == 5:
        return prac5.sortedPrimeNumbers
    if num == 6:
        return prac6.getStatistics
    if num == 7:
        return prac7.matchings
    if num == 8:
        return prac8.rps
    return None


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1:
        print('Call second argument to number')
        print('$ python3 judge.py {number}')
        sys.exit()
    num = 0
    try:
        num = int(argv[1])
    except:
        print('Second arguments is not number!')
    anspac.generator.generateAnswer(num, practice(num))
