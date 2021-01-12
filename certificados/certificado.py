from xlrd import open_workbook
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd
import os

def gera_certificado(nome_certificado, nome_arquivo):
    nome_do_arquivo_certificado = 'certificado_' + nome_arquivo.replace(' ', '_') + '.png'
    imagem_certificado = Image.open('certificados\\cet.png')
    imagem_certificado_desenho = ImageDraw.Draw(imagem_certificado)
    fonte_certificado = ImageFont.truetype("arial.ttf", 25)
    fonte = ImageFont.truetype("arial.ttf", 15)

    text = "Escrevendo um texto, para testar o certificado, \nEmitido no dia 17/12/2020, na capacitacao \
    \nTeste X Wordpress com Python Ahora"

    imagem_certificado_desenho.text((400, 300), nome_certificado, font=fonte_certificado, fill=(0, 0, 0))
    imagem_certificado_desenho.text((400, 350), text, font=fonte, fill=(0, 0, 0))
    imagem_certificado.save(nome_do_arquivo_certificado, 'PNG', resolution=100.0)
    return nome_do_arquivo_certificado

if __name__ == '__main__':

    planilha_inscricoes = open_workbook('certificados\\students.xlsx')

    '''planilha_inscricoes = pd.read_excel(
        'certificados\\students.xlsx',
        engine='openpyxl'
    )'''
    folha_planilha_inscricoes = planilha_inscricoes.sheet_by_index(0)


    for i in range(1, folha_planilha_inscricoes.nrows):
        aluno_nome_certificado = folha_planilha_inscricoes.row_values(i)[3]
        aluno_nome_arquivo = folha_planilha_inscricoes.row_values(i)[2]

        nome_certificado = gera_certificado(aluno_nome_certificado, aluno_nome_arquivo)
