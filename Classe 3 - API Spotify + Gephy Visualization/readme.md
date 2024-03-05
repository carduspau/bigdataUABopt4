# Classe 3 - API Spotify + Gephy Visualization
> 27/02/2024
> 
Obtenir les relacions dels generes entre els artistes relacionats obtinguts a la classe anterior. S'emmagatzema les dades en un CSV i mitjançant pandas en un dataframe amb "source" i "target" que son els que Gephi interpretarà per mostrar l'esquema graph i podrem veure les relacions entre aquests generes en base als artistes.

**Artista origen:** "Segismundo Toxicómano"

_main.py_
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/c940e094-72a7-494a-8f9a-1df1198473ab)

### Tasques 
#### 1) Incloure gèneres musicals al dataset i visualitzar les relacions mitjançant un Graph > _tasca1.py_
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/a978f106-1207-4993-b0f4-b76519c97a18)

<img src="https://cdn-icons-png.freepik.com/512/10748/10748293.png" width="40px">

#### 2) Fer el mateix procés d'obtenció pero a partir d'una playlist. > _tasca2.py_
<img src="https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/e2c03681-a282-402a-82c8-bcf45531b578" width="500px"> <br>

El procés consistia en "alimentar" la funció treballada fins ara: _artist_related_artist(artist_id)_ passant com a argument l'artist_id obtingut dinàmicament desde un bucle for mitjançant una altra funció de l'API anomenada: _playlist_items(playlist_id)_.
S'ha utilitzat la playlist "!Arriba los ánimos!", generada pel propi Spotify formada per 80 cançons. <br><br> M'ha semblat interessant estudiar quins artistes i gèneres considera Spotify que pujaran el nostre estat anímic. En aquest cas hi ha 3 que destaquen: 
- Pop / Dance Pop
- Soul
- Rock / Soft Rock
- Reggueton / Urbano (tenen una agrupació modular molt separada a la resta pero amb un tamany a considerar)

#### 3) Generar el graph 

![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/2f015f05-fef0-43f5-b6f8-862a33235bce)

<hr>

#### 4) Crear JSON's de playlist utilitzant l'offset i processar-los després de recopilar-los
- import json
- import glob

### Tecnologies i llibreries noves que hem utilitzat: 

|               | Tecnologia/Llibreria | Definició i ús                             |
|-----------------------|-----------------------|----------------------------------------|
| <img src="https://gephi.org/gephi-lite/gephi-logo.svg" width="200px"> | Gephi                 | Eina de visualització de xarxes i gràfics, utilitzada per analitzar, explorar i visualitzar dades de xarxes complexes. Ampla aplicació en ciència de les xarxes, visualització de dades i investigació social. En el nostre cas com es vee a les captures, l'hem fet servir per fer visualitzacions interactives i veure les relacions entre artistes i gèneres mitjançant nodes |
| GLOB LIBRARY | glob                 | Llibreria que permet obtenir informació dels fitxers de la carpeta i emmagatzar en un array filtrant amb instruccions com en el nostre cas que hem obtingut només els .json (`*:json`) |




