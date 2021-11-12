SB2 - String builder SB extension  

    dependency: SB (see above)
    
    Preserve indexes in the original string
    
    methods:
        sb = SB() or SB(s)
        freese_ind() - preseve current indexes
                       [ if omitted, SB2 == SB ]
        add(s) or append(s) - add s to the end
        prepend(s)
        ins(s, ind) - insert using, 'original' ind
        delete([size=], ind=) - size by default is 1, 'original' ind
        repl_to(s [,size=], ind=) - replace sub-string by s, based on 'original' ind;
                                    size by default is the same as len(s)
        
        clear() - reset sb
    
    properties:
        ind - return current 'real' index in sb
        str - return current string in sb
        
   sample:
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
    
 console log:
SB2. : original str: abcd
1. prepend 'XYZ': XYZabcd
2. replaced abc->ABC: XYZABCd
3. replaced ABC->1234: XYZ1234d
4. appended 'XYZ': XYZ1234dXYZ
---using original indexes:
5. a-> A: Abcdefgh
6. b-> BB: ABBcdefgh
7. c-> CCC: ABCCCcdefgh
8. d-> DDD: ABCCDDDcdefgh
9. g-> GGG: ABCCDDDcdefGGGh
9. BB-> BBB: ABBBCDDDcdefGGGh
 --- replacing by smaller tokens ----
10. original: aBBBcDDDefg
11. BBB-> b: abcDDDefg
12. delete DDD: abcefg
Warning: part of substring ind:2 size:2 was deleted ... skip
13. attempt to replace deleted earlier BB, no change: abcefg
14. c-> CCC: abCCCefg
 --- insert/delete ----
15. original: aBBBcDDDefg
16. insert 123 after a: a123BBBcDDDefg
16. insert 456 after c: a123BBBc456DDDefg
17. delete 123 after a: aBBBc456DDDefg
Warning: part of substring ind:2 size:2 was deleted ... skip
18. attempted to delete again, no change: aBBBc456DDDefg
    