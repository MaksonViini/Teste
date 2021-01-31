class Carro:
    def __init__(self, vel_max, ligado, cor):
        self.vel_max = vel_max
        self.ligado = ligado
        self.cor = cor
    
    def mostra_atributos(self):
        print(self.vel_max)
        print(self.ligado)
        print(self.cor)

c1 = Carro(300, True, 'Azul')

c1.mostra_atributos()