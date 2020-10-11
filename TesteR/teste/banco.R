library("DBI")

con = dbConnect(RMySQL::MySQL(),
                dbname = "painel",
                host = 'localhost',
                user = 'root',
                password = '', 
                #port = '3306', 
                )
#dbDisconnect(con)
