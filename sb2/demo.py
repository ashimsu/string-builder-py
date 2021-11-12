# --------------------------------------

from  sb2 import *
  
def test_sb2():
    sb = SB2('abcd')
    print("SB2. : original str:", sb.str)
    sb.freese_ind()
    sb.prepend('XYZ')      
    print("1. prepend 'XYZ':", sb.str)
    sb.repl_to('ABC', ind = 0)
    print("2. replaced abc->ABC:",sb.str)   # orig. ind 0, current 3
    sb.repl_to('1234', size = 3, ind = 0)
    print("3. replaced ABC->1234:",sb.str)   # orig. ind 0, current 3
    sb.append('XYZ')
    print("4. appended 'XYZ':",sb.str)
    
    print('---using original indexes:')
    sb.clear()
    sb.add('abcdefgh')
    sb.freese_ind()
    sb.repl_to('A', ind = 0)
    print("5. a-> A:",sb.str)
    sb.repl_to('BB', size = 1, ind = 1)
    print("6. b-> BB:",sb.str)
    sb.repl_to('CCC', size = 1, ind = 2)
    print("7. c-> CCC:",sb.str)
    sb.repl_to('DDD', size = 1, ind = 3)
    print("8. d-> DDD:",sb.str)
    sb.repl_to('GGG', size = 1, ind = 6)
    print("9. g-> GGG:",sb.str)
    sb.repl_to('BBB', size = 2, ind = 1)
    print("9. BB-> BBB:",sb.str)
    
    print(' --- replacing by smaller tokens ----')
    sb.clear()
    sb.add('aBBBcDDDefg')
    print("10. original:",sb.str)
    sb.freese_ind()
    sb.repl_to('b', size=3, ind = 1)  # delete (BB)
    print("11. BBB-> b:",sb.str)
    sb.repl_to('', size = 3, ind = 5)
    print("12. delete DDD:",sb.str)   # delete (DDD)
    sb.repl_to('!!', ind = 2) 
    print("13. attempt to replace deleted earlier BB, no change:",sb.str)
    sb.repl_to('CCC', size = 1, ind = 4)
    print("14. c-> CCC:",sb.str)
    
    print(' --- insert/delete ----')
    sb.clear()
    sb.add('aBBBcDDDefg')
    print("15. original:",sb.str)
    sb.freese_ind()
    sb.ins('123', ind = 1)
    print("16. insert 123 after a:",sb.str)
    sb.ins('456', ind = 5)
    print("16. insert 456 after c:",sb.str)
    sb.delete(size=3, ind=1)
    print("17. delete 123 after a:",sb.str)
    sb.delete(size=2, ind=2)
    print("18. attempted to delete again, no change:",sb.str)
    
     
            
def main():
    test_sb2()
    
if __name__ == '__main__':
    main()
    exit(0)
