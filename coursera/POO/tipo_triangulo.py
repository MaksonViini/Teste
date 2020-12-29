class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        elif self.a != self.b and self.b != self.c:
            return 'escaleno'
        else:
            return 'isósceles'

t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5).tipo_lado()
# deve devolver 'escaleno'