@author = Pol Gubau Amores

notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

# Columna 1: Nombre y apellidos (en una única cadena de texto) de cada alumno
# Columna 2: Nota de cada alumno
# Columna 3: Nota "en texto" para cada alumno:
# Si la nota final es inferior a 5, añadir el texto "suspendido".
# Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".
# Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".
# Si la nota es igual o superior a 7, añadir el texto "notable".
# Si la nota supera el 9, añadir el texto "Excelente".
# Si la nota equivale a un 10, añadir el texto "matrícula de honor".
# Columna 4: Diferencia de nota respecto a la mediana del grupo
# Columna 4: Diferencia de nota (expreseda en porcentaje) respecto a la mediana del grupo


# Condiciones especiales
# Antes de hacer los cálculos, debes sumar UN punto a cada alumno, pero la nota máxima nunca puede superar el 10.


# Importamos la librería pandas
import pandas as pd 


# Creamos un dataframe con las listas de alumnos, apellidos y notas
dataframe = pd.DataFrame(
    {
        'Alumne': alumnes, 
        'Cognom': cognoms,
        'Nota': notes
    }
)

dataframe['Alumne'] = dataframe['Alumne'] + ' ' + dataframe['Cognom']

# eliminamos la columna de apellidos
dataframe = dataframe.drop(columns=['Cognom'])

dataframe['Nota'] = dataframe['Nota'] + 1 # le suamamos 1 a cada nota

dataframe['Nota'] = dataframe['Nota'].apply(lambda x: 10 if x > 10 else x) # si la nota es mayor que 10, la nota es 10, si no, la nota es la misma

dataframe['Nota en Text'] = dataframe['Nota'].apply(lambda x: 'Matrícula de honor' if x == 10 else 'Excelente' if x > 9 else 'Notable' if x >= 7 else 'Bien' if x >= 6 else 'Aprobado' if x >= 5 else 'Suspendido')


dataframe['Diferencia'] = dataframe['Nota'] - dataframe['Nota'].median()

dataframe['Diferencia %'] = dataframe['Diferencia'] / dataframe['Nota'].median() * 100 

# redondear la media a 2 decimales
dataframe['Diferencia %'] = dataframe['Diferencia %'].apply(lambda x: round(x, 2))



print ('Mediana del grupo:', dataframe['Nota'].median())

print(dataframe)

# download the file as csv
dataframe.to_csv('ex1.csv', index=False)
