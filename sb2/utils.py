
''' return true if 1-st range has intersection with the second'''
from typing_extensions import TypeVarTuple

'''' return true if ranges intersect '''
def has_intersect(i1:int, sz1:int, i2:int, sz2:int):
        if (i1 >= i2 and i1 <  i2 + sz2) or (i2 >= i1 and i2 <  i1 + sz1):
            return True
        return False
    
'''' return true if ranges are adjacent '''
def are_adjasent(i1:int, sz1:int, i2:int, sz2:int):
    if ((i1 <= i2 and i1 + sz1 == i2) or (i2 <= i1 and i2 + sz2 == i1)):
            return True
    return False    
        
'''' return combined range from 2 intersected ranges'''  
def combine_intersect(i1:int, sz1:int, i2:int, sz2:int):
    if (i1 <= i2 and i1 + sz1 == i2):
        return(i1, i2 - i1 + sz2)
    elif (i2 <= i1 and i2 + sz2 == i1):
        return(i2, i1 - i2 + sz1)

''' combine adjacent ranges '''
def combine_ranges(i1:int, sz1:int, i2:int, sz2:int):
    if has_intersect(i1, sz1, i2, sz2):
        return combine_intersect(i1, sz1, i2, sz2)
    elif are_adjasent(i1, sz1, i2, sz2):
        return (min(i1,i2, sz1 + sz2))
    
