# Classe 5 - PANDAS
'''Objetivo: Crea un documento .CSV con 5 columnas:

Columna 1: Nombre y apellidos (en una única cadena de texto) de cada alumno
Columna 2: Nota de cada alumno
Columna 3: Nota "en texto" para cada alumno:
Si la nota final es inferior a 5, añadir el texto "suspendido".
Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".
Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".
Si la nota es igual o superior a 7, añadir el texto "notable".
Si la nota supera el 9, añadir el texto "Excelente".
Si la nota equivale a un 10, añadir el texto "matrícula de honor".
Columna 4: Diferencia de nota respecto a la mediana del grupo
Columna 4: Diferencia de nota (expreseda en porcentaje) respecto a la mediana del grupo
Condiciones especiales
Antes de hacer los cálculos, debes sumar UN punto a cada alumno, pero la nota máxima nunca puede superar el 10.
'''

import pandas as pd

notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]

dicc = {}
llista_noms_cognoms = []

for i in range(len(alumnes)):
    nom_cognom = f'{alumnes[i]}  {cognoms[i]}'  # Added space after comma
    llista_noms_cognoms.append(nom_cognom)

print(llista_noms_cognoms)

def increment(notes):
    notes_arreglades = []
    for nota in notes:
        if nota < 10:
            nota += 1
        notes_arreglades.append(nota)
    return notes_arreglades

def to_text(notes_arreglades):
    notes_text = []
    for nota in notes_arreglades:
        if(nota<5):
            nota = "Suspendido"
            notes_text.append(nota)
        elif(nota>=5 and nota<= 6):
            nota = "Aprovado"
            notes_text.append(nota)
        elif(nota>6 and nota <7):
            nota = "Bien"
            notes_text.append(nota)
        elif(nota>=7 and nota <9):
            nota = "Notable"
            notes_text.append(nota)
        elif(nota>=9 and nota <10):
            nota = "Excelente"
            notes_text.append(nota)
        elif(nota==10):
            nota = "Matricula"
            notes_text.append(nota)
    return notes_text


'''Columna 4: Diferencia de nota respecto a la mediana del grupo
Columna 4: Diferencia de nota (expreseda en porcentaje) respecto a la mediana del grupo'''

def diferenia_mediana(notes_arreglades):
    mitjana_notes = notes_arreglades.sum() /len(notes_arreglades)

    return mitjana_notes

def diferencia_mediana_percent():



notes_arreglades = increment(notes)
notes_text = to_text(notes_arreglades)

print (notes_arreglades)
print(notes_text)






'''
df = pd.DataFrame(),
df = pd.DataFrame.from_dict()


output = to_dataframe().to_csv('output.csv',sep=";", index=False)'''

