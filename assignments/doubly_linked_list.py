class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
    def __str__(self):
        return f'{self._value}'
        
class LinkedList:
    def __init__(self):
        self._first=None
        self._tail = None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
            self._tail = self._first
        else: # add to the end of a non-empty list
            new_node = Node(value, previous=self._tail)
            self._tail._next = new_node
            self._tail = new_node

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def __len__(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
    def get_node(list,index):
        n=list._first
        for i in range(index):
            n=n._next
            if n==None:
                return None
        else:
            return n
        
    def get(list,index):
       return list.get_node(index)._value

    def set(list,index,value):
        n = list.get_node(index)
        if not n:
            return
        n._value=value

    def insert(list, index, value):
        if len(list)==index:
            new_node = Node(value, previous=list._tail)
            list._tail._next = new_node
            list._tail = new_node
            return
        
        y = list.get_node(index)
        
        if not y:
            return

        x=y._previous

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            list._first=new_node

        if y._next == None:
            list._tail = new_node

        y._previous=new_node

    def remove(list, index):
        n = list.get_node(index)
        if not n:
            return 
        
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            list._first=y

        if y:
            y._previous=x
        else:
            list._tail = x
        return n._value
    
    def clear(self):
        temp = self._first
        while temp!=None:
            self.remove(0)
            temp = temp._next
    def count(self, data):
        temp = self._first
        count = 0
        while temp != None:
            if(temp._value == data):
                count += 1
            temp = temp._value
        return count
    
    def __str__(self):
        output = '('
        temp = self._first
        while temp != None:
            output += str(temp._value) + ','
            temp = temp._next
        output +=')'
        return output

    def __contains__(self, data):
        temp = self._first
        while temp != None:
            if temp._value == data:
                return True
            temp = temp._next
        return False

    def __getitem__(self,index):
        n=self._first
        for i in range(index):
            n=n._next
            if n==None:
                return None
        else:
            return n