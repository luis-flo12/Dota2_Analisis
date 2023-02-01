# Dota2_Analisis
### Usando OpenDota API en Python para el analisis de datos de la ultima temporada de la DPC-SA
<img src="https://github.com/luis-flo12/Dota2_Analisis/blob/main/DPC-SA-ESB.jpeg?raw=true" width="840" height="560">

## Indice

1. [Introducción](#intro)  
2. [Tareas](#tasks)
3. [Data Extraction](#dataextraction)  
4. [Análisis](#modeling)
5. [Descripción de los archivos](#files)

## 1. Introducción  <a name="intro"></a>
DOTA es uno de los juegos MOBA competitivos más famosos del mundo. Dota es un juego querido por sus jugadores alrededor del mundo y especialmente por la comunidad peruana, ya que es uno de los juegos que más influencia ha tenido dentro de la escena competitiva de los E-sports. Todos los días, millones de jugadores entran en la batalla como uno de los más de cien héroes de DOTA en un choque de equipos 5v5. Cada jugador controla un Héroe, una unidad estrategicamente poderosa con habilidades y caracteristicas únicas que se pueden fortalecer a medida que el juego continue.

Siendo un fanatico de la escena competitiva del DOTA sudamericano, sabia que existia un paquete para R "RDota2" y un paquete para Python "dota2". Mediante estos paquetes se pueden acceder a los datos del juego a través de una API. Desde que descubrí esto, siempre quise jugar con los datos del juego y analizar los "trends" y estrategías de los equipos profesionales.

Por ello, en este proyecto se tratará de utilizar los datos extraidos de la API OpenDota para analizar los datos de "Picks", "Bans" y "Win Rate" de los heroes escogidos durante la ultima temporada de la DPC-SA(torneo comparable con la primera división del futbol peruano). Mediante este analisis se busca comprender un poco más las estrategias utilizadas por los profesionales y entender un poco más el "Metagame" actual.

## 2. Tareas <a name="tasks"></a>

Como ya he comentado, este proyecto tratará de analizar la data extraida del juego y proveer graficos que puedan ser facilmente entendibles. Para realizar dicho objetivo se organizarón las siguientes tareas:
- Extraer los ID de las partidas de la ultima DPC-SA
- Extraer la data de la API OpenDota
- Analizar la data y generar los graficos.

## 3. Data Extraction <a name="dataextraction"></a>

OpenDota es una API open-source con la cual puedes tener acceso a data del juego. Desde partidas publicas, partidas profesionales, información de los heroes, equipos, etc. De esta manera, OpenDota se convierte en una herramienta muy poderosa para el analisis de información relacionada con el DOTA. Como referencia del API pueden entrar al siguiente link [OpenDota API](https://docs.opendota.com/).

### Obtener Partidas Profesionales  

El primer obstaculo que encontre en este proyecto fue encontrar el ID de las partidas profesionales. Si bien es posible obtener las ID's de las partidas de manera manual dentro del juego, esto es muy tedioso y tomaria mucho tiempo. Para resolver este problema hice uso de la libreria BeautifulSoup para obtener los ID's de la pagina [DotaBuff](https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports).

```python
from bs4 import BeautifulSoup as BS
import requests, json, time, os
url = ["https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&series_status=live_or_completed" , "https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&page=2&series_status=live_or_completed", "https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&page=3&series_status=live_or_completed","https://es.dotabuff.com/esports/leagues/14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports/matches?original_slug=14886-dpc-2023-sa-winter-tour-division-i-presented-by-esb-liga-esports&page=4&series_status=live_or_completed"]
headers = {
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}
matches_id = []
for i in url:
    r=requests.get(i, headers=headers)
    soup = BS(r.text,'lxml')
    for x in soup.select('article a[href*="/matches/"]'):
        matches_id.append(x.text)

```
Una vez obtenidas las ID's de las partidas que nos interesan, hice uso de la API para obtener la información de las partidas y las guarde en varios archivos json.
  
```python
for u in matches_id:
    data = requests.get("https://api.opendota.com/api/matches/"+ u)
    #print("Get:",u)
    partidas= data.json()
    #Guardamos la data
    file = open(u + '_partidas.json','x')
    json.dump(partidas,file)
    file.close()

```  

### Obtener el Dataset de los Héroes  

En el dataset que obtuvimos en la sección anterior, cada heroe esta representado por un integer unico(Números del 1 al 121) llamado "hero_id". Por ello, es necesario obtener el dataset de los heroes para hallar el string que representa su nombre del heroe dentro del juego.

```python
import requests, json, time, os
import pandas as pd
# Buscamos la información de los heroes
data = requests.get("https://api.opendota.com/api/heroes").json()
outfile= open('hero_stats.json','w')
json.dump(data,outfile)
pd.DataFrame(data).to_csv("hero_stats.csv",sep=",")

```
La data de los héroes puedes encontrarla como "hero_stats.csv" dentro de repositorio. 

## 4. Análisis<a name="modeling"></a>

El proceso de obtención de los datos esta dentro de los siguientes archivos: [Picks](https://github.com/luis-flo12/Dota2_Analisis/Dota2_tables.py) y [Bans](https://github.com/luis-flo12/Dota2_Analisis/Dota2_banned.py)

Durante este proyecto se logró analizar la data concerniente a los "Picks" ,"Bans" y "Winrate" de los heroes escogidos en la ultima temporada de la DPC-SA. Los graficos obtenidos son bastante esclarecedores, ya que se puede observar que hay cierta correlación entre los Picks y Bans y el Winrate de cada heroe. Los héroes con mayor Winrate tienen una alta probabilidad de tambien estar presentes en los graficos de Most Picked o Most Banned. Esto concuerda con lo que se ve dentro de las partidas profesionales donde los equipos escogen a los heroes más poderoso o evitan que el otro equipo los pueda escoger mediante un ban. 

Se muestran los graficos obtenidos:
<img src="https://github.com/luis-flo12/Dota2_Analisis/blob/main/10_Highest_Winrates.png?raw=true" width="840" height="560">

<img src="https://github.com/luis-flo12/Dota2_Analisis/blob/main/10_Most_Picked.png?raw=true" width="840" height="560">
 
<img src="https://github.com/luis-flo12/Dota2_Analisis/blob/main/Top10_most_banned.png?raw=true" width="840" height="560">
