library("DBI")
library(leaflet)

con = dbConnect(RMySQL::MySQL(),
              dbname = 'teste',
               host = 'localhost',
              user = 'root',
               password = ''
)

dbListTables(con)

df = data.frame(lat = runif(40, min = -19.8157, max = -19.80), 
                lng = runif(40, min = -43.9542, max = -43.94))

#states = geojsonio::geojson_read("https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json", what = "sp")

df2 = dbGetQuery(con, "select lat, lng from mapa")


#head(df)
df2
#lat = -19.8157
#lng = -43.9542


df2 %>% leaflet() %>% addTiles() %>% 
  addCircleMarkers(clusterOptions = markerClusterOptions()) %>% 
  setView(df2, lat = -19.8157, lng = -43.9542, zoom=12)
  

  


#my_map = leaflet() %>% addTiles()
#my_map = my_map %>% addMarkers(lat=vetor_lat, lng=vetor_long, popup = 'Teste')
#my_map
