class Jar:
    def __init__(self, capacity, n):
        
        self.capacity = capacity
        self = n
        
    def __str__(self):
        
        if int(self.capacity) <= 0:
            raise ValueError("Baitch ass!")

        cookie = "🍪"
        if self.n == 0:
            cookie = ""
        more_cookies  = "🍪"
        for i in range(self.n - 1):
            cookie = cookie + more_cookies
        return cookie


print(Jar(input("Capacity: "), 0))





#Deposit adds n cookies to jar. If deposit > Capasity. Raise ValueError
#withdraw removes n cookies from jar. If withdraw > Jar. Raise Value error
#Capacity returns jar capacity
#Size returns n cookies in jar.

#Object oriented programming er å sette en class med funksjoner som kan bli kallen på.
#Dette hjør det enklere å køyre funksjoner via class istadenfor å holde kontroll på alle samtidig.
