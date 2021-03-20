from datetime import date, time, datetime


class Dates:
    def trabalhando_com_date():
        data_atual = date.today()

        # Formatando data para dia mes ano
        print(data_atual.strftime('%d/%m/%y\n'))

        # Formatando data para dia, mes e ano na forma escrita
        print(data_atual.strftime('%A %B %Y\n'))

    def trabalhando_com_time():
        horario = time(hour=15, minute=18, second=20)
        print(horario.strftime('%H:%M:%S\n'))

    def trabalhando_com_datetime():
        data_atual = datetime.today()
        print(data_atual, '\n')
        print(data_atual.strftime('%d/%m/%y %H:%M:%S\n'))

        # Trazendo o dia atual traduzido a partir do indice da tupla
        tupla = ('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
        print(tupla[data_atual.weekday()])


# if __name__ == '__main__':
dates = Dates
dates.trabalhando_com_date()
dates.trabalhando_com_time()
dates.trabalhando_com_datetime()
