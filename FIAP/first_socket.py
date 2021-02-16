import socket

resp = "S"
while(resp == 'S'):
    url = str(input('Digite uma url: '))
    ip = socket.gethostbyname(url)
    print(f'O ip referente a url informada e: {ip}')
    resp = str(input('Digite [S] para continuar').upper())