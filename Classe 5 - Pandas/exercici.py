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
Antes de hacer los cálculos, debes sumar UN punto a cada alumno, pero la nota máxima nunca puede superar el 10.'''

import pandas as pd

notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]

llista_noms_cognoms = []
for i in range(len(alumnes)):
    nombre_apellido = alumnes[i] + ' ' + cognoms[i]
    llista_noms_cognoms.append(nombre_apellido)

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
        if nota < 5:
            nota_texto = "Suspendido"
        elif 5 <= nota <= 6:
            nota_texto = "Aprobado"
        elif 6 < nota < 7:
            nota_texto = "Bien"
        elif 7 <= nota < 9:
            nota_texto = "Notable"
        elif 9 <= nota < 10:
            nota_texto = "Excelente"
        elif nota == 10:
            nota_texto = "Matricula"
        notes_text.append(nota_texto)

    return notes_text

def diferencia_mitjana(notes_arreglades):
    mitjana_notes = round(sum(notes_arreglades) / len(notes_arreglades))
    diferencia_mitj = []
    for nota in notes_arreglades:
        diferencia = nota - mitjana_notes
        diferencia_mitj.append(diferencia)

    return diferencia_mitj

def diferencia_mitjana_percent(notes_arreglades):
    mitjana_notes = round(sum(notes_arreglades) / len(notes_arreglades))
    porcentajes_mitj = []
    for nota in notes_arreglades:
        diferencia = nota - mitjana_notes
        porcentaje = (diferencia / mitjana_notes) * 100
        porcentajes_mitj.append(porcentaje)

    return porcentajes_mitj

# ejecutar funciones
notes_arreglades = increment(notes)
notes_text = to_text(notes_arreglades)
diferencia_mitjana = diferencia_mitjana(notes_arreglades)
diferencia_percent_mitjana = diferencia_mitjana_percent(notes_arreglades)

dicc = {}
llista_final = []

for i in range(len(alumnes)):
    dicc = {
        "Nom i cognoms ": alumnes[i] + ' ' + cognoms[i],
        "Nota alumne (nº)": notes_arreglades[i],
        "Avaluació ": notes_text[i],
        "Diferencia de nota respecte la mitjana ": diferencia_mitjana[i],
        "Diferencia de nota (%) respecte la mitjana ": diferencia_percent_mitjana[i]
    }
    llista_final.append(dicc)

df = pd.DataFrame(llista_final)
df.to_csv('alumnos_final.csv', index=False)


