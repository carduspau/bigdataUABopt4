from pytrends.request import TrendReq
import plotly.express as px
import pandas as pd

# Conectar con Google Trends
pytrends = TrendReq(hl='es', tz=360)

# Construir la carga útil para buscar en YouTube
kw_list = ["ahorrar"]
pytrends.build_payload(kw_list, cat=0, timeframe='2005-01-01 2024-01-01', geo='ES', gprop='youtube')

# Interés a lo largo del tiempo
data = pytrends.interest_over_time()
data = data.reset_index()

# Guardar los datos en un archivo CSV
data.to_csv("ahorrar.csv", index=False)

# Crear el gráfico
fig = px.line(data, x="date", y=kw_list, title='Interés de Búsqueda en YouTube a lo largo del Tiempo')
fig.show()
