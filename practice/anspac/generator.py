'''
{'writer': 'Takuma Matsumoto', 'date': '22/3/2018'}
'''

from anspac import judgers

def generateAnswer(num, func):
    with open('anspac/cases' + str(num) + '.csv', 'r') as input:
        with open('anspac/table' + str(num) + '.csv', 'w') as output:
            for arg in input.readlines():
                ans = judgers.func(num, func, arg)
                output.write(arg.strip() + ' -> ' + str(ans) + '\n')
