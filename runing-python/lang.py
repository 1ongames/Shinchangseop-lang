import sys
from run import Reboot2

class Reboot:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        for line in code.splitlines():
            self.process_line(line)

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
        if '5천플' in code:
            return '+'
        if '5천마' in code:
            return '-'
