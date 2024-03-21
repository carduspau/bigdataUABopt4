# clase 6

# Llibreries a instal·lar #

import requests
from bs4 import BeautifulSoup

import pandas as pd
import time
import glob

#scrapping
def extract_wiki():
    for anyo in range(2000,2024):
        resposta = requests.get(f'https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{anyo}')
        try:
            codi_web = resposta.text
            soup = BeautifulSoup(codi_web, 'html.parser')

            final = soup.find('span', id='Final')
            print(final)
            tabla = final.find_next("table")
            df = pd.read_html(str(tabla))[0]
            print(df)
            print(f'Todo bien en {anyo}')
            df.to_excel(f'datasetEurovision-{anyo}.xlsx', index=False)
            time.sleep(1)
        except(AttributeError):
            print(f"Problema en {anyo}")

#extract_wiki()



files = glob.glob("*.xlsx")
list_dfs = []

for f in files :
    df = pd.read_excel(f)
    any = f.split('-')[1].split('.')[0]
    list_dfs.append(df)
    df['año'] = any
    df.columns.values[2] = "Cantante(s)"
    df.columns.values[5] = "Puntos"
    df.columns.values[0] = "N."
final_df = pd.concat(list_dfs)
final_df.to_excel("final.xlsx", index=False)



