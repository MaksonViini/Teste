def maiusculas(frase):
    texto = list(frase)
    caracter = ""
    for item in texto:
        c = ord(item)
        if c >= 65 and c <= 90:
            caracter += item
    return caracter

print(maiusculas('Programamos em Python 2?'))