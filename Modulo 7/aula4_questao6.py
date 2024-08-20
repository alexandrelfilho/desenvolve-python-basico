import pandas as pd

# Carregar o arquivo CSV com encoding 'latin-1'
file_path = 'spotify-2023.csv'
data = pd.read_csv(file_path, encoding='latin-1')

# Filtrar colunas necessárias
data = data[['track_name', 'artist(s)_name', 'released_year', 'streams']]

# Filtrar por anos de 2012 a 2022
data = data[(data['released_year'] >= 2012) & (data['released_year'] <= 2022)]

# Filtrar linhas com problemas (artista(s) entre aspas, o que indica um problema com a formatação)
# Usamos a verificação para identificar as linhas que têm campos de texto com vírgulas.
data = data[~data['track_name'].str.contains('"', na=False)]
data = data[~data['artist(s)_name'].str.contains('"', na=False)]

# Convertendo streams para numérico, erros de conversão são convertidos para NaN
data['streams'] = pd.to_numeric(data['streams'], errors='coerce')

# Encontrar a música mais tocada de cada ano
most_streamed_per_year = data.loc[data.groupby('released_year')['streams'].idxmax()]

# Gerar a lista final com as informações solicitadas
result = most_streamed_per_year[['track_name', 'artist(s)_name', 'released_year', 'streams']].values.tolist()

# Exibir a lista
print(result)
