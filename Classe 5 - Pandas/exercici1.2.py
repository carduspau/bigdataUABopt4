'''En este dataset tienes los datos extraídos del canal de YouTube "KEXP" en formato xlsx. La "KEXP" (Seattle International) es una emisora con una larga tradición de conciertos en directo. El dataset contiene todos los vídeos publicados hasta el 11/03/2024. Queremos saber:

    1. Volumnen general: ¿Cuantas filas y columnas tiene el dataset completo?
    2. Composición del dataset: ¿Qué columnas componen el dataset?
    3. Calcula la desviación (absoluta y porcentual) de cada vídeo sobre el promedio de especatadores/comentarios/likes del canal.
    4. Localiza el vídeo más visto.
    5. Localiza el vídeo más comentado.
    6. rea una nueva columna para cada uno de los valores calculador anteriormente, y crea un nuevo dataset final que incorpore toda la nueva información.
    7. Calcula la duración en segundos de cada video, e indica su desviación porcentual sobre el promedio de duración de los videos del canal.
    8. Visualiza todas las estadísticas calculadas anteriormente en un gráfico de Tableau'''

import pandas as pd

# 1. Volumnen general: ¿Cuantas filas y columnas tiene el dataset completo?
df = pd.read_csv("dataset.csv")
print(len(df))

# 2. Composición del dataset: ¿Qué columnas componen el dataset?
print(df.columns)

# 3. Calcula la desviación (absoluta y porcentual) de cada vídeo sobre el promedio de especatadores/comentarios/likes del canal.

average_views = df['viewCount'].mean()
average_comments = df['commentCount'].mean()
average_likes = df['likeCount'].mean()


df['desviacio_absoluta_likes'] = df['likeCount'] - average_likes
df['desviacio_absoluta_comments'] = df['commentCount'] - average_comments
df['desviacio_absoluta_views'] = df['viewCount'] - average_views

df['desviacio_%_likes'] = (df['likeCount'] - average_likes )/ average_likes * 100
df['desviacio_%_comments'] = (df['commentCount'] - average_comments )/ average_comments * 100
df['desviacio_%_views'] =(df['viewCount'] - average_views )/ average_views * 100

#4. Localiza el vídeo más visto.
row_max_view_video = df.iloc[[df['viewCount'].idxmax()]]
print(row_max_view_video)

#5. Localiza el vídeo más comentado.
row_max_comment_video = df.iloc[[df['commentCount'].idxmax()]]
print(row_max_comment_video)

#6. Crea una nueva columna para cada uno de los valores calculador anteriormente, y crea un nuevo dataset final que incorpore toda la nueva información.
df = df.drop(['channelId', 'categoryId', 'channelTitle', 'tags', 'publishedAt', 'blocked_at'], axis=1)
df.to_csv("final.csv")

#7. Calcula la duración en segundos de cada video, e indica su desviación porcentual sobre el promedio de duración de los videos del canal.
#### Pendent de fer a classe amb una comprovació del docent







