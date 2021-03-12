class Televisao:
    def __init__(self):
        self.ligado = False
        self.canal = 5

    def power(self):
        self.ligado = self.ligado != True

    def up_canal(self):
        self.canal += 1

    def low_canal(self):
        self.canal -= 1


tv = Televisao()

print(tv.ligado)

tv.power()

print(tv.ligado)
