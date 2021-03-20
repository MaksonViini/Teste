from datetime import date, time

class Dates:
    def trabalhando_com_date():
        data_atual = date.today()

        # Formatando data para dia mes ano
        print(data_atual.strftime('%d/%m/%y'))

        # Formatando data para dia, mes e ano na forma escrita
        print(data_atual.strftime('%A %B %Y')) 


    def trabalhando_com_time():
        horario = time(hour=15, minute=18, second=20)


# if __name__ == '__main__':
dates = Dates
dates.trabalhando_com_date()
dates.trabalhando_com_time()