peso = float(input("Informe seu peso: "))
idade = int(input("Informe sua idade: "))
sexo = str(input("Informe seu sexo: "))

if idade > 0 and idade < 3:
    if sexo in "Ff":
        print(f"Sua necessidades energéticas e de {61 * peso - 51} kcal ")
    else:
        print(f"Sua necessidades energéticas e de {60.9 * peso - 54} kcal ")

elif idade >= 3 and idade < 10:
    if sexo in "Ff":
        print(f"Sua necessidades energéticas e de {22.5 * peso + 499} kcal ")
    else:
        print(f"Sua necessidades energéticas e de {22.7 * peso + 495} kcal ")

elif idade >= 10 and idade < 18:
    if sexo in "Ff":
        print(f"Sua necessidades energéticas e de {12.2 * peso + 746} kcal ")
    else:
        print(f"Sua necessidades energéticas e de {17.5 * peso + 651} kcal ")

elif idade >= 18 and idade < 30:
    if sexo in "Ff":
        print(f"Sua necessidades energéticas e de {14.7 * peso + 496} kcal ")
    else:
        print(f"Sua necessidades energéticas e de {15.3 * peso + 679} kcal ")

elif idade >= 30 and idade < 60:
    if sexo in "Ff":
        print(f"Sua necessidades energéticas e de {8.7 * peso + 829} kcal ")
    else:
        print(f"Sua necessidades energéticas e de {11.6 * peso + 879} kcal ")

elif idade > 60:
    if sexo in "Ff":
        print(f"Sua necessidades energéticas e de {10.5 * peso + 596} kcal ")
    else:
        print(f"Sua necessidades energéticas e de {13.5 * peso + 487} kcal ")
