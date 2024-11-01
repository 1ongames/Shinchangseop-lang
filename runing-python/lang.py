import sys

class Reboot:
    def __init__(self):
        self.data = [0]*256

    def toNumber(self, code):
        tokens = code.split(' ')
        result = 1
        for token in tokens:
            num = (self.data[token.count('어') - 1] if token.count('어') else 0) + token.count('.') - token.count(',')
            result *= num
        return result

    def lang(code):
        if '오늘도' in code:
            return 'import'
        