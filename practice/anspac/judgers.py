'''
{'writer': 'Takuma Matsumoto', 'date': '22/3/2018'}
'''

from anspac.referee import Referee
import ast

def func(num, func, vals):
    '''
    Defines how to call practice functions
    e.g.
        def practice1(num): # return triple of argument
            return num * 3

    ->  if num == 1:
            return func(int(vals))
    '''
    if num == 1:
        return func()
    if num == 2:
        return func(ast.literal_eval(vals))
    if num == 3:
        return func(vals.strip())
    if num == 4:
        return func(vals.strip())
    if num == 5:
        return func(ast.literal_eval(vals))
    if num == 6:
        return func(ast.literal_eval(vals))
    if num == 7:
        li = ast.literal_eval(vals)
        return func(li[0], li[1])
    if num == 8:
        li = ast.literal_eval(vals)
        return func(li[0], li[1])

def judge(num, prac, path):
    referee = Referee(path)
    if not referee.table:
        return
    accept = True
    qtexts = referee.table.keys()
    count = 1
    for ques in qtexts:
        print('case', count, ': ', end='')
        ans = func(num, prac, ques)
        case_accepted = referee.judge(ques, ans)
        if case_accepted:
            print('accept')
        else:
            accept = False
            print('wrong answer')
            if ques:
                print(' input:', ques)
            print(' output:', ans)
        count += 1

    print('Clear!' if accept else 'Failure...')
