class Carro:
    def __init__(self, vel_max, ligado, cor):
        self.vel_max = vel_max
        self.ligado = ligado
        self.cor = cor
    
    def mostra_atributos(self):
        print(self.vel_max)
        print(self.ligado)
        print(self.cor)

    def altera_atributos(self, vel_max=300, ligado=True, cor='Azul'):
        self.vel_max = vel_max
        self.ligado = ligado
        self.cor = cor

c1 = Carro(300, True, 'Azul')

c1.mostra_atributos()
c1.altera_atributos(1, False)
c1.mostra_atributos()

