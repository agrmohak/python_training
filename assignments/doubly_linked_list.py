class Node:
    def __init__(self, data,next=None, previous=None):
        self._data=data
        self._next=next
        self._previous=previous
    def __str__(self):
        return f'{self._data}'
    def __repr__(self) -> str:
        return self.__str__()
        
class LinkedList:
    def __init__(self):
        self._first=None
        self._tail = None
        self.__len = 0
    class Iterator:
        def __init__(self, list):
            self._list=list
            self._current=None
            
        def __next__(self):
            if not self._current:
                self._current=self._list._first
            else:
                self._current=self._current._next
                
            if self._current:
                return self._current._data
            else:
                raise StopIteration()
    def __iter__(self):
        return LinkedList.Iterator(self)

    def append(self, *args):
        for x in args:
            self._append(x)
        
    def _append(self, data):
        if self._first==None: # list is empty
            self._first=Node(data)
            self._tail = self._first
        else: # add to the end of a non-empty list
            new_node = Node(data, previous=self._tail)
            self._tail._next = new_node
            self._tail = new_node
        self.__len += 1

    def __len__(self):
        return self.__len
    def __get_node(self,index):
        for i, data in enumerate(self):
            if i == index:
                return data
        else:
            raise IndexError('list index out of range')

    def set(self,index,data):
        n = self.__get_node(index)
        if not n:
            return
        n._data=data

    def insert(self, index, data):
        if len(self)==index:
            new_node = Node(data, previous=self._tail)
            self._tail._next = new_node
            self._tail = new_node
            return
        
        y = self.__get_node(index)
        
        if not y:
            return

        x=y._previous

        new_node=Node(data,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            self._first=new_node

        if y._next == None:
            self._tail = new_node

        y._previous=new_node

    def remove(self, index):
        n = self.__get_node(index)
        if not n:
            return 
        
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            self._first=y

        if y:
            y._previous=x
        else:
            self._tail = x
        return n._data
    
    def clear(self):
        temp = self._first
        while temp!=None:
            self.remove(0)
            temp = temp._next
    def count(self, data):
        count = 0
        for x in self:
            if x == data:
                count +=1
        return count
    
    def __str__(self):
        output = '['
        for x in self:
            output += str(x)
            if(x!=None):
                output += ', '
        output +=']'
        return output
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __contains__(self, data):

        for x in self:
            if x == data:
                return True
        return False

    def __getitem__(self,indexer):
        pos = indexer
        if type(pos) == int and indexer < 0:
            pos = self.__len + indexer
        return self.__get_node(pos)