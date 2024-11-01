import sys
# TODO: 더 쉽게 사용할 수 있게
# from run import Reboot2

class Reboot:
 # 여기부터   
    def __init__(self):
        self.data = [0]*256

    def toNumber(self, code):
        tokens = code.split(' ')
        result = 1
        for token in tokens:
            num = (self.data[token.count('시') - 1] if token.count('시') else 0) + token.count('.') - token.count(',')
            result *= num
        return result

# 여기까지 엄랭 코드
    @staticmethod
    def lang(code):
        if '오늘도' in code:
            return 'import'
        if '메벤' in code:
            return 'from'
        if '신창섭' in code:
            return 'if'
        if '김창섭' in code:
            return 'else'
        if '신김창섭' in code:
            return 'elif'
        if '쌀먹' in code:
            return 'print'
        if '과징금' in code:
            return 'while'
        if '본섭' in code:
            return 'for'
        if '인장' in code:
            return '#'
# 여기는 엄랭 참고
    def jungsanghwa(self, code)
        if code = '':
            raise SyntaxError('코드가 없네 씨 발 년')
        decode = self.lang(code)

        if decode == 'import':
            
        
    
