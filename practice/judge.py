'''
{'writer': 'Takuma Matsumoto', 'date': '22/3/2018'}
'''

import sys
from anspac import judgers
import question

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
    judgers.judge(num, question.practice(num), 'anspac/table' + str(num) + '.csv')
