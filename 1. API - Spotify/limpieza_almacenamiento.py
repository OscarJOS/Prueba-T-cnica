import pandas as pd
#Leo el archivo CSV.
df = pd.read_csv('Songs.csv', sep=';')

df['Genres'] = df['Genres'].replace('\[', '', regex=True)
df['Genres'] = df['Genres'].replace('\]', '', regex=True)
df['Genres'] = df['Genres'].replace("\'", '', regex=True)

#Separo la columna de genero y la agrupo por nombre de canción.
new_df = pd.DataFrame(df.Genres.str.split(',').tolist(), index=df["Song Name"]).stack()
new_df = new_df.reset_index([0, 'Song Name'])
new_df.columns = ['Song Name', 'Genres']
#Agrupo por DataFrame y recorro cada uno, selecciono 'Song Name', lo convierto en un CSV y le doy como nombre el género.
for genre, df in new_df.groupby('Genres'):
    df['Song Name'].to_csv('{}.csv'.format(genre), index=False, header = False)
