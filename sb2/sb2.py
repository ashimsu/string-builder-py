''' String builder SB2

    dependency: SB1
    
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
'''

import os.path, sys

path = os.path.join( os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sb')
sys.path.insert(0, path)

from sb import *
    
class SB2(SB):
    def __init__(self, s: str = ''):
        SB.__init__(self, s)
        self.orig_ind_ = False
        self.map_ = []          # map of indices
        self.del_ = []          # map of deleted indices
        
    def freese_ind(self):
        if len(self.lst) > 0:
            self.orig_ind_ = True
            self.map_ = [(0,0)]
        else:
            self.orig_ind_ = False
            self.map_.clear() 

    def prepend(self, tkn:str):
        if self.orig_ind_:
            x,y = self.map_[0]
            self.map_[0] = (x, y + len(tkn))
        super(SB2, self).prepend(tkn)
    
    def append(self, tkn:str):
        super(SB2, self).append(tkn)
        
    def add(self, tkn:str):
        self.append(tkn)
        
    def __find_in_map__(self, ind:int):
        for i in range(len(self.map_)):
            if self.map_[i][0] >= ind:
                return i
            i+=1
        return None
    
    def __is_between__(self, i1, sz1, i2, sz2):
        if (i1 >= i2 and i1 <  i2 + sz2) or (i2 >= i1 and i2 <  i1 + sz1):
            return True
        return False
    
    def __find_in_del__(self, ind, size):
        for x in self.del_:
            if self.__is_between__(x[0], x[1], ind, size):
                return True
        return False
            
    def __find_offset__(self, ind):
        offs = 0
        for i in range(len(self.map_)):
            if self.map_[i][0] > ind:
                break
            offs += self.map_[i][1]
        return offs
    
    def __upd_del__(self, ind, size_dif):
        for i in range(len(self.del_)):
            x,y = self.del_[i]
            if x > ind :
                self.del_.insert(i, (ind, size_dif))
                return
            elif x <= ind and ind <  x  + y:
                self.del_[i] = (min(x, ind), max(y, size_dif))
                return 
            i+=1
        self.del_.append((ind, size_dif)) 
        
    def ins(self, tkn:str = '', ind:int=-1 ):
        ''' insert '''
        if not self.orig_ind_:
            return super(SB2, self).ins(tkn, ind)
        self.repl_to(tkn, size = 0, ind = ind)
        
    def delete(self, size:int=1, ind:int = -1):
        ''' delete '''
        if not self.orig_ind_:
            return super(SB2, self).delete(size = size, ind = ind)
        self.repl_to(tkn = '', size = size, ind = ind)    
        
    def repl_to(self, tkn:str = '', size:int=-1, ind:int = -1):
        ''' replace sub-string ( + inseert or delete ) '''
        if not self.orig_ind_:
            return super(SB2, self).repl_to(ind, tkn, size)
        
        if ind < 0:
            return self.prepend(tkn)
        if ind >= self.sz:
            return self.append(tkn)
        
        if size < 0:
            size = len(tkn)
            
        if self.__find_in_del__(ind, size):
            print(f"Warning: part of substring ind:{ind} size:{size} was deleted ... skip")
            return
         
        offs = self.__find_offset__(ind)    
        sz_ = min(self.sz - ind, size)   
        size_dif = len(tkn) - sz_
        if size_dif != 0:
            map_i = self.__find_in_map__(ind + len(tkn))
            if map_i:
                if self.map_[map_i][0] == ind + sz_:
                    x,y = self.map_[map_i]
                    self.map_[map_i] = (x, y + size_dif)
                else:
                    self.map_.insert(map_i, (ind + sz_, size_dif))
            else:
                self.map_.append((ind + sz_, size_dif))
            
            if size_dif < 0:
                self.__upd_del__(ind + sz_, -size_dif)
                    
        
        super(SB2, self).repl_to(tkn, size = size, ind = ind + offs)
    
    def clear(self):
        self.map_.clear()
        self.del_.clear()
        super(SB2, self).clear()
