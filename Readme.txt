Prueba técnica Simetrik

Descripción

1. API - Spotify
Descripción del problema
Para este reto se necesita obtener el top de canciones de Colombia divididas por
género (Cada genero tiene que ser un archivo csv). La extracción de los datos
debe ser de la API de Spotify. Link API: https://developer.spotify.com/

Comentarios:
- Para este ejercicio utilicé la playlist:
    -> Colombia Top 50 url= https://open.spotify.com/playlist/37i9dQZEVXbOa2lmxNORXQ
- Este ejercicio lo dividí en dos partes:
    1. Extracción de datos. Archivo: extraccion_datos.py
        - Para ejecutar este archivo se necesita tener instalado:
            - spotipy
            - pandas
    2. Limpieza y almacenamiento. Archivo: limpieza_almacenamiento.py
        - Para ejecutar este archivo se necesita tener instalado:
            - pandas

Nota 1: Debido al formato que entrega la API Spotipy no tenemos la información
del género musical al que pertenece una canción cuando extraemos el JSON de la
playlist. Por esto, debemos buscar el género musical en otra referencia. Yo lo
encontré en Artista, en donde cada artista tiene una lista de géneros a la cual
es asociado. Por esto toca hacer otra petición en donde traemos una lista de
géneros para cada artista.
Ver = https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/


2. Prueba de texto
Descripción del problema
El segundo reto consiste en extraer la información de un archivo de texto con
columnas de espacios fijos, el archivo csv final debe contar con 4 columnas
(marca; tipo; ubicación, placa), y agregar las columnas de: 
    1. fecha: 06/07/2019
    2. consecutivo: consecutivo en el número de transacción

Comentarios:
- Para ejecutar este archivo se necesita tener instalado:
    - pandas
    - numpy

Nota 2: Con el metodo read_fwf de pandas puedo leer archivos de texto con
columnas de espacios fijos y le paso el parametro "widths" para darle el tamaño
de las columnas. Con "encoding" soluciono el problema de las tildes. Con
"dtype=str" almaceno las placas con los ceros iniciales. Con "names" le doy el
nombre de las columnas en orden.


3. Consumo Prueba
Descripción del problema
Adjunto enviamos el archivo “consumo_prueba_2019.xls”, este archivo tiene la
información de las estaciones en una fila (00 SOL, 01 AIRES…) esta fila tiene
que ser una columna del dataframe (Estacion), y el entregable es un csv. En la
imagen está cómo debería quedar el dataframe.

Comentarios:
- Para ejecutar este archivo se necesita tener instalado:
    - pandas

    


Oscar Forero
