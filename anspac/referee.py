'''
{'writer': 'Takuma Matsumoto', 'date': '22/3/2018'}
'''

class Referee:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            list = [x.strip().split('-> ') for x in f.readlines()]
            self.table = dict(list)

    def judge(self, input, output):
        return self.table[str(input)] == str(output)
