library("DBI")
library(RODBC)
library(odbc)

con = dbConnect(RMySQL::MySQL(),
               dbname = "painel",
               host = 'localhost',
                user = 'root',
                password = '', 
                port = '3306', 
               )
#dbDisconnect(con)
#sort(unique(odbcListDrivers()[[1]]))

###con = dbConnect(odbc::odbc(),  .connection_string= "Server=localhost, 
               ##Database=painel, UID=root;
               #Driver={SQL Server Native Client 11.0};") 

#con <- dbConnect(odbc::odbc(), .connection_string = "Server=nomeDoServidor;
               #  Database=nomeDoBancoDeDados;UID=usuario;
              #   PWD=senha;Driver={SQL Server Native Client 11.0};")


#con = odbcConnect("MSSQL")


