1. SB - string builder 

 methods:
    sb = SB() or SB(s)
    add(s) or append(s) - add s to the end
    prepend(s)
    ins(s [,ind=]) - insert; ind by default is 'current' position in sb 
    delete([size=] [,ind=]) - size by default is 1, ind - is'current' 
    repl_to(s [,size=] [,ind=]) - replace sub-string by s; 
                                  size by default is the same as len(s), ind - is 'current' 
    clear() - reset sb
    curr_ind([+/-delta]|[start=True]|[end=True]) - change 'current' position  

 properties:
     ind - current index
     str - return current string in sb
         
testing parms: -t: performance check, -h help
   
sample:
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
   
console log:
PS C:\projpy\learn> python s07sb1.py
SB. original str: [aXYbcdefg]
1. deleted 'XY': [abcdefg]
   current ind': 2
2. inserted 'PQR' after a: [aPQRbcdefg]
3. deleted 'PQ': [aRbcdefg]
4. deleted 'R': [abcdefg]
5. inserted 'INS' after a: [aINSbcdefg]
6. replaced c by 'REPL': [aINSbREPLdefg]
7. added '_Append': [aINSbREPLdefg]_Append
8. pre-pended 'Prepend_': Prepend_[aINSbREPLdefg]_Append
   current ind : 8  (after Prepend_)
   changed current ind by -4, now: 4
9. replaced end to END': PrepEND_[aINSbREPLdefg]_Append
   reset current ind, now: 0
10. replaced P to p: prepEND_[aINSbREPLdefg]_Append
11. ...
