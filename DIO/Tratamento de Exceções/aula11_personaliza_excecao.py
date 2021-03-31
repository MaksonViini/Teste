class Error(Exception):
    pass


class InputError(Error):

    def __init__(self, message):
        self.messege = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        if x > 10:
            raise InputError('Nota nao pode ser maior que 10!')

        elif x < 0:
            raise InputError('Nota nao pode ser menor que 0!')

        print(f'A nota digitada foi {x}')
        break

    except ValueError:
        print('Valor invalido!')

    except InputError as ex:
        print(ex)
