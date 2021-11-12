''' python -m pytest -q tests.py '''

from sb2 import *

sb = SB2()

class Test_sb:
      
    def test1(self):
        sb.add('abcdefg')
        sb.freese_ind()
        sb.repl_to('BBB',size = 1, ind = 1)
        assert sb.str == 'aBBBcdefg'
        sb.repl_to('DDD',size = 1, ind = 3)
        assert sb.str == 'aBBBcDDDefg' 