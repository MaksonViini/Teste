library("DBI")
library(leaflet)

#con = dbConnect(RMySQL::MySQL(),
 #              dbname = 'painel',
  #              host = '127.0.0.1',
  #             user = 'root',
   #             password = ''
#)

#dbListTables(con)

df = data.frame(lat = runif(20, min = -19.81, max = -19.8), 
                lng = runif(20, min = -43.95, max = -43.9))

states = geojsonio::geojson_read("https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json", what = "sp")

class(states)

names(states)

head(df)
lat = -19.8157
lng = -43.9542

df %>% leaflet() %>% addTiles() %>% 
  addCircleMarkers(clusterOptions = markerClusterOptions())

  


#	Latitude: -19.8157 Longitude: -43.9542
#my_map = leaflet() %>% addTiles()
#my_map = my_map %>% addMarkers(lat=vetor_lat, lng=vetor_long, popup = 'Teste')
#my_map
