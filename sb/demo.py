''' String Builder demo'''

from sb import *

# ----------------test methods ------------ #       
def test_sb():
    sb = SB('[aXYbcdefg]')              # or sb = SB(); sb.add('...')
    print("SB. original str:", sb.str)
    sb.repl_to('', size=2, ind=2)       # or: repl_to('', 2, 2)     
    print("1. deleted 'XY':",sb.str )
    print("   current ind':", sb.ind)
    sb.ins('PQR')                       # use curr index (ind=2)
    print("2. inserted 'PQR' after a:",sb.str)
    sb.delete(2, ind=2)                 # delete size=2
    print("3. deleted 'PQ':",sb.str)
    sb.delete()                         # use current index (ind=2), delete size by default is 1)    
    print("4. deleted 'R':",sb.str)
    sb.ins('INS')                       # use current index (ind=2)
    print("5. inserted 'INS' after a:",sb.str)
    sb.repl_to('REPL', size=1, ind=6)   # or ('REPL', 1, 6)
    print("6. replaced c by 'REPL':",sb.str)
    sb.append('_App')
    sb.add('end')
    print("7. added '_Append':",sb.str)
    sb.prepend('Prepend_')
    print("8. pre-pended 'Prepend_':",sb.str)
    print("   current ind :", sb.ind , " (after Prepend_)")
    sb.curr_ind(-4)
    print("   changed current ind by -4, now:", sb.ind)
    sb.repl_to('END')
    print("9. replaced end to END':",sb.str)
    sb.curr_ind(start=True)
    print("   reset current ind, now:", sb.ind)
    sb.repl_to('p')
    print("10. replaced P to p:",sb.str)
    sb.prepend(' 1234567890' * 20)
    print("11. pre-pended long string:",sb.str)
    sb.add(' 9876543210' * 20)
    print("12. append long string:",sb.str)
    
# ----------------test performance ------------ #
def test_sb_time():
    ''' compare performance, regular vs SB '''
    import time
    
    repeat = 20000
    
    start_tm1 = time.time()

    for i in range(repeat):
        s = 'aXYbcdefg'  
        s1  = s[:1] + s[3:]
        s2  = s1[:1] + 'INS' + s1[1:]
        s3  = s2[:5] + 'REPL' + s2[6:]
        s4  = s3 + '_App'
        s5  = s4 +'end'
        s6  = 'Prepend_'+ s5
    print(s6)
          
    print(f"Elapsed time (reg): {round(time.time() - start_tm1, 4)} sec. Repeated {repeat} times ")  
    
    start_tm2 = time.time()
    
    sb = SB() 
    for i in range(repeat):
        sb.clear()
        sb.append('aXYbcdefg')
        sb.delete(size=2, ind=1)      
        sb.ins('INS', 1)                   
        sb.repl_to('REPL', size=1, ind=5)
        sb.append('_App')
        sb.add('end')
        sb.prepend('Prepend_')
        
    print(sb.str)   
    print(f"Elapsed time (sb): {round(time.time() - start_tm2, 4)} sec. Repeated {repeat} times")
    
''' usage: parms: -t: performance check, -h help '''        
def main(argv):
    if '-t' in argv:
        test_sb_time()
    elif '-h' in argv:
        print('usage: parms: -t: performance check, -h help') 
    else:
        test_sb()
         
if __name__ == '__main__':
    import sys
    
    main(sys.argv[1:])
    exit(0)

# --- methods --- #       
def test_sb():
    sb = SB('[aXYbcdefg]')              # or sb = SB(); sb.add('...')
    print("SB. original str:", sb.str)
    sb.repl_to('', size=2, ind=2)       # or: repl_to('', 2, 2)     
    print("1. deleted 'XY':",sb.str )
    print("   current ind':", sb.ind)
    sb.ins('PQR')                       # use curr index (ind=2)
    print("2. inserted 'PQR' after a:",sb.str)
    sb.delete(2, ind=2)                 # delete size=2
    print("3. deleted 'PQ':",sb.str)
    sb.delete()                         # use current index (ind=2), delete size by default is 1)    
    print("4. deleted 'R':",sb.str)
    sb.ins('INS')                       # use current index (ind=2)
    print("5. inserted 'INS' after a:",sb.str)
    sb.repl_to('REPL', size=1, ind=6)   # or ('REPL', 1, 6)
    print("6. replaced c by 'REPL':",sb.str)
    sb.append('_App')
    sb.add('end')
    print("7. added '_Append':",sb.str)
    sb.prepend('Prepend_')
    print("8. pre-pended 'Prepend_':",sb.str)
    print("   current ind :", sb.ind , " (after Prepend_)")
    sb.curr_ind(-4)
    print("   changed current ind by -4, now:", sb.ind)
    sb.repl_to('END')
    print("9. replaced end to END':",sb.str)
    sb.curr_ind(start=True)
    print("   reset current ind, now:", sb.ind)
    sb.repl_to('p')
    print("10. replaced P to p:",sb.str)
    sb.prepend(' 1234567890' * 20)
    print("11. pre-pended long string:",sb.str)
    sb.add(' 9876543210' * 20)
    print("12. append long string:",sb.str)
    
# --- performance --- #
def test_sb_time():
    ''' compare performance, regular vs SB '''
    import time
    
    repeat = 20000
    
    start_tm1 = time.time()

    for i in range(repeat):
        s = 'aXYbcdefg'  
        s1  = s[:1] + s[3:]
        s2  = s1[:1] + 'INS' + s1[1:]
        s3  = s2[:5] + 'REPL' + s2[6:]
        s4  = s3 + '_App'
        s5  = s4 +'end'
        s6  = 'Prepend_'+ s5
    print(s6)
          
    print(f"Elapsed time (reg): {round(time.time() - start_tm1, 4)} sec. Repeated {repeat} times ")  
    
    start_tm2 = time.time()
    
    sb = SB() 
    for i in range(repeat):
        sb.clear()
        sb.append('aXYbcdefg')
        sb.delete(size=2, ind=1)      
        sb.ins('INS', 1)                   
        sb.repl_to('REPL', size=1, ind=5)
        sb.append('_App')
        sb.add('end')
        sb.prepend('Prepend_')
        
    print(sb.str)   
    print(f"Elapsed time (sb): {round(time.time() - start_tm2, 4)} sec. Repeated {repeat} times")
    
''' usage: parms: -t: performance check, -h help '''        
def main(argv):
    if '-t' in argv:
        test_sb_time()
    elif '-h' in argv:
        print('usage: parms: -t: performance check, -h help') 
    else:
        test_sb()
         
if __name__ == '__main__':
    import sys
    
    main(sys.argv[1:])
    exit(0)
    