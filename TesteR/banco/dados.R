library("DBI")

con = dbConnect(RMySQL::MySQL(),
                dbname = 'painel',
                host = '127.0.0.1',
                user = 'root',
                password = ''
)

dbListTables(con)

