class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro_veio = Carro("Ferrari", 2020, "Preto")
print(carro_veio.cor)