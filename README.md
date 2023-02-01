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
