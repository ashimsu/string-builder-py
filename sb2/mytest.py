# --------------------------------------

from  sb2 import *
  
def test_sb2():
    sb = SB2('abcdefg')
    print("SB2. : original str:", sb.str)
    sb.freese_ind()
    sb.delete(2, ind=3)      
    print("1. del 2:", sb.str, sb.ind)
    sb.repl_to('D', size=2, ind=3) 
    print("2. ins D:", sb.str, sb.ind) 
   
    
         
def main():
    test_sb2()
    
if __name__ == '__main__':
    main()
    exit(0)
