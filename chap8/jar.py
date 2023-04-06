    #capacity > 0. __init__ should initialize this int
    #__str__ returns a str with n cookies as an emoji
    #Deposit adds n cookies to jar. If deposit > Capasity. Raise ValueError
    #withdraw removes n cookies from jar. If withdraw > Jar. Raise Value error
    #Capacity returns jar capacity
    #Size returns n cookies in jar.

    #Object oriented programming er å sette en class med funksjoner som kan bli kallen på.
    #Dette hjør det enklere å køyre funksjoner via class istadenfor å holde kontroll på alle samtidig.

import sys

#    @property
#    def capacity(self):
#        return self.capacity
#
#    @capacity.setter
#    def capacity(self, capacity):
#        if int(capacity) <= 0:
#            raise ValueError
#        self.capacity = capacity


class Jar:
    def __init__(self, capacity = 12):
        if int(capacity) <= 0:
            raise ValueError('Wrong capacity')
        self._capacity= capacity
        self.size = 0
        
    def __str__(self):
        return self.size * '🍪'

    
    def deposit(self, n):
            if n > self.capacity:
                raise ValueError('Exceeded Capacity!')
            if self.size + n > self.capacity:
                raise ValueError('Exceeded Capacity!')
            self.size += n
    
    def withdraw(self, n):
        if self.size < n:
            raise ValueError('Too few cookies')
        self.size -= n
        
    
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Bitch Ass!")
        if value > self._capacity:
            raise ValueError("Nick Guhrr")
        self._size = value
    
jar = Jar(12)
jar.deposit(9)
print(jar.size)
jar.withdraw(3)