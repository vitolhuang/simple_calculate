class OperateModel:
    def __init__(self):
        self.sum = '0'

    def operate(self, value):
        if value == 'AC':
            self.sum = '0'
        elif value == '=':
            self.sum = eval(self.sum)
        else:
            if self.sum == '0':
                self.sum = f'{value}'
            else:
                self.sum = f'{self.sum}{value}'

    def GetValue(self):
        return str(self.sum)
