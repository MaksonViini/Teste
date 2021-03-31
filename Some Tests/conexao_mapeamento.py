import mysql.connector

mydb = mysql.connector.connect(
  host="mysql742.umbler.com",
  user="ezef7nmuhnzk",
  password="yH94vvE68Mcw"
)

print(mydb)


cursor = mydb.cursor()
sql = "INSERT INTO mapeamento (RELATO_MAO_LIVRE, RELACAO_AGRESSORDATA, LOCAL, DESCRICAO_LOCAL, IDADE_DATA_FATO, IDADE_ATUAL, TIPO_VIOLENCIA, RELIGIAO, IDENTIDADE_GENERO, ORIENTACAO_SEXUAL, SEXO, ESCOLARIDADE, PROFISSAO, NACIONALIDADE, ETNIA, DEFICIENCIA, VIOLENCIA_INSTITUCIONAL, FEZ_DENUNCIA, MOTIVO_NAO_DENUNCIA) VALUES (x, nenhuma, 12/11/2020, Avenida Abílio Machado, Uma avenida, 19, 30, outra, dasd, dsd, cis, Feminino, Ensino fundamental, Cantora, Brasileira, Branca, nao, nao, sim, sdsd"

cursor.execute(sql)

mydb.commit()

print(cursor.rowcount, "record inserted.")