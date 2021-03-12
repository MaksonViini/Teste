class Televisao:
    def __init__(self):
        self.ligado = False

    def power(self):
        self.ligado = self.ligado != True

    
tv = Televisao()

print(tv.ligado)

tv.power()

print(tv.ligado)