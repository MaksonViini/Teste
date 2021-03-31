# Programa da Talitinha
from random import randint
from time import sleep
i = randint(0, 12)
temas = ['Mobilidade urbana sustentável', 'A evasão escolar em questão no Brasil',
'O meio ambiente em questão no Brasil', 'O perigo da crise hídrica no Brasil', 'Analfabetismo total e funcional', 
'O trabalho na construção da dignidade humana', 'Viver em rede no século 21: os limites entre o público e o privado',
'A persistência da violência contra a mulher na sociedade brasileira', 
'Os impactos psicológicos do uso das redes sociais pelos jovens', 'A importância e os desafios da oferta de educação financeira nas escolas do Brasil', 
'Homeschooling - vantagens e desvantagens da educação à distância para a formação básica', 'Os perigos da automedicacao no Brasil', 
'Perigos do lixo eletronico para o meio ambiente'
]
sleep(1)
print('BOA')
sleep(1)
print('SORTEEEEEE!')
print('O tema sorteado foi...'.upper())
print('-=-'*15)
print(temas[i])
print('-=-'*15)
#print('BOA SORTE TALITINHA <3 <3 <3!!!')