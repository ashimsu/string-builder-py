''' string builder v.2'''

class SB:
    '''string builder
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
         
    '''
    def __init__(self, s: str = None):
        self.sz = 0
        self.buf_sz = 1
        self.lst = []
        self.append(s)
        self.curr_ind_ = self.sz                      # current position
    
    def __extend_buf__(self, min_sz:int): 
        if min_sz < 128:
            buf_sz = 128
        elif min_sz < 256:
            buf_sz = 256
        elif min_sz < 512:
            buf_sz = 512
        elif min_sz < 1024:
            buf_sz = 1024
        else:
            buf_sz = min_sz + 1024
        
        if self.buf_sz < buf_sz:
            self.lst.extend([None] * (buf_sz - self.buf_sz))
            self.buf_sz = buf_sz
    
    def __check_buf_sz__(self, added_sz:int):
        ''' check buffer size before adding a token, expand if needed'''
        if self.sz + added_sz > self.buf_sz:
           self.__extend_buf__(self.sz + added_sz)
    
    def __put__(self, tkn:str, ind:int):
        ''' put token into self.lst starting from position ind '''
        i  = 0
        for x in tkn:
            self.lst[ind + i] = x
            i += 1       
        
    def append(self, tkn:str):
        ''' attach token to end  '''
        if tkn:
            self.__check_buf_sz__(len(tkn))
            self.__put__(tkn, self.sz)
            self.sz += len(tkn)
            self.curr_ind_ = self.sz
        
    def add(self, tkn:str):
        ''' same as append '''
        self.append(tkn)
    
    def prepend(self, tkn:str):
        self.__check_buf_sz__(len(tkn))
        self.__shift_right__(0, len(tkn))
        self.__put__(tkn, 0)
        self.curr_ind_ = len(tkn)
             
    def clear(self):
        ''' reset sb '''
        self.lst.clear()
        self.__init__('')
        
    def __shift_right__(self, ind:int, size:int = 1):
        ''' move part of the self.lst to the right, from position ind '''
        self.lst[self.sz + size: ind + size : -1] = self.lst[self.sz: ind: -1]
        self.lst[ind + size] = self.lst[ind]
        self.sz += size

    def __shift_left__(self, ind:int, size:int = 1):
        ''' delete part of the self.lst; i.e move left starting from ind + size position '''
        self.lst[ind: self.sz - size] = self.lst[ind+size: self.sz]
        self.sz -= size
        
    def __repl__(self, ind:int = 0, tkn:str = '', size:int=-1):
        ''' replace /insert / delete / append /pre-pend
            ind < 0 - pre-pend; ind > self.lst size - append
            token = '' - delete; size = 0 - insert
        '''
        if ind < 0:
            return self.prepend(tkn)
        if ind >= self.sz:
            return self.append(tkn)
             
        sz_ = min(self.sz - ind, size) if size >= 0 else min(self.sz - ind, len(tkn))   
        size_dif = len(tkn) - sz_
        
        if size_dif > 0:
            self.__check_buf_sz__(size_dif)
            self.__shift_right__(ind, size_dif) 
        elif size_dif < 0:   
            self.__shift_left__(ind, -size_dif) 
            
        self.__put__(tkn, ind)
        self.curr_ind_ = ind + len(tkn)
        
    def ins(self, tkn:str = '', ind:int=-1 ):
        ''' insert '''
        self.__repl__(ind = self.curr_ind_ if ind < 0 else ind, tkn = tkn, size = 0)
        
    def delete(self, size:int=1, ind:int = -1):
        ''' delete '''
        self.__repl__(ind = self.curr_ind_ if ind < 0 else ind, tkn = '', size = size)
    
    def repl_to(self, tkn:str = '', size:int=-1, ind:int = -1):
        ''' replace sub-string ( + inseert or delete ) '''
        self.__repl__(ind = self.curr_ind_ if ind < 0 else ind, tkn = tkn, size = size)
    
    ''' return current index '''
    @property
    def ind(self):
        return self.curr_ind_
    
    ''' set current index'''
    def curr_ind(self, delta = 0, end = False, start = False):
        if start:
            self.curr_ind_ = 0
        elif end:
             self.curr_ind_ = self.sz
        else:   
            self.curr_ind_ = self.curr_ind_ + delta
            if self.curr_ind_ < 0:
                self.curr_ind_ = 0
            elif self.curr_ind_ > self.sz:
                self.curr_ind_ = self.sz
                        
    @property   
    def str(self):
        return ''.join(self.lst[0: self.sz])

