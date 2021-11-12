''' python -m pytest -q tests.py '''

from sb import *

sb = SB()

class Test_sb:
      
    def test1(self):
        sb.add('[abXYcdefg]')
        assert sb.str == '[abXYcdefg]'
        sb.delete(2,ind=3)
        assert sb.str == '[abcdefg]'
        
    def test2(self):
        sb.curr_ind(end = True)
        sb.curr_ind(-1)
        sb.repl_to(')')
        sb.curr_ind(start = True)
        sb.repl_to('(')
        assert sb.str == '(abcdefg)'
        sb.ins('XYZ', 4)
        assert sb.str == '(abcXYZdefg)'
        assert(sb.ind == 7)
        sb.curr_ind(-3)
        sb.delete(3)
        assert sb.str == '(abcdefg)'
        assert(sb.ind == 4)
        sb.ins('TUV')
        assert sb.str == '(abcTUVdefg)'
        sb.repl_to('', size = 3, ind = sb.ind - 3)
        assert sb.str == '(abcdefg)'
      
    def test3(self):
        sb.prepend('Pfx_')
        sb.add('_Sfx')
        assert sb.str == 'Pfx_(abcdefg)_Sfx'
        sb.curr_ind(start = True)
        sb.delete(4)
        assert sb.str == '(abcdefg)_Sfx'
        sb.curr_ind(end= True)
        sb.repl_to('', size = 4, ind = sb.ind - 4)
        assert sb.str == '(abcdefg)'
                    