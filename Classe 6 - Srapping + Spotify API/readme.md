# Classe 6 - Web Scrapping + Spotify API 
> 19/03/2024

En aquest codi s'automatitza la recopilació i organització de dades sobre el Festival de la Cançó d'Eurovisió des de la Viquipèdia i les guarda en un format convenient per a un posterior anàlisi o visualització. (.xlsx en aquest cas) 

<hr>

**Exercici 1 (main.py)**
- Utilitza web scraping per extreure dades de la pàgina de la Viquipèdia sobre el Festival de la Cançó d'Eurovisió per a cada any des del 2000 fins al 2023.
- Després de recopilar les dades, les emmagatzema en un arxiu Excel separat per a cada any amb el format "datasetEurovision-{anyo}.xlsx".
- Seguidament, llegeix els arxius Excel creats i els combina en un únic dataframe.
- Modifica els noms de les columnes i afegeix una nova columna amb l'any de cada conjunt de dades.
- Finalment, guarda el dataframe combinat en un nou arxiu Excel anomenat "final.xlsx".

_Exemple dataset 2002_:
  > ![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/faaf885a-b0b6-4b36-b224-965f97779b6b)

**Exercici 2 (main2.py)**
- Llegeix el dataframe obtingut al exercici anterior del fitxer "final.xlsx".
- Per a cada fila del dataframe, realitza una cerca a través de l'API de Spotify utilitzant informació com el cantant, la cançó i l'any del Festival d'Eurovisió. Els resultats de la cerca s'emmagatzemen en un fitxer JSON anomenat "search.json".
  ![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/ccb20c7b-f1f8-4a26-8aef-1b29f1c05840)
- Es pausa l'execució durant 15 segons després de cada cerca per evitar superar els límits d'ús de l'API de Spotify. (poden ser menys segons, els 15 son per fer comprovacions del primer resultat amb tranquilitat).

### Tecnologies i llibreries noves que hem utilitzat: 

|               | Tecnologia/Llibreria | Definició i ús                             |
|-----------------------|-----------------------|----------------------------------------|
| <img src="https://gephi.org/gephi-lite/gephi-logo.svg" width="200px"> | Gephi                 | Eina de visualització de xarxes i gràfics, utilitzada per analitzar, explorar i visualitzar dades de xarxes complexes. Ampla aplicació en ciència de les xarxes, visualització de dades i investigació social. En el nostre cas com es vee a les captures, l'hem fet servir per fer visualitzacions interactives i veure les relacions entre artistes i gèneres mitjançant nodes |
| GLOB LIBRARY | glob                 | Llibreria que permet obtenir informació dels fitxers de la carpeta i emmagatzar en un array filtrant amb instruccions com en el nostre cas que hem obtingut només els .json (`*:json`) |
