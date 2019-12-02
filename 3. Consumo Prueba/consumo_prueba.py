import pandas as pd
df = pd.read_excel('consumo_prueba_2019.xls', sheet_name = 'rptListadoConsumoClientes', skiprows = range(1, 7))
df = df.dropna(axis=1, how='all')
df.columns = df.iloc[1]
df = df[df.Cliente != 'Cliente'].reset_index(drop=True)
df = df[~df.Factura.str.contains('No.+', regex=True, na=False)].reset_index(drop=True)
estaciones = df["Cliente"].dropna()
estaciones = estaciones[:-1]
df = df.drop(['Cliente'], axis = 1)
df = df.loc[:, df.columns.notnull()]
df["Tiquete"] = df["Factura"]
df = df.dropna(how='all')
df["Factura"] = estaciones[1]
df["Factura"] = df["Factura"].str.replace("\\n", "",regex=True)
df["Fecha"] = df["Fecha"].dt.strftime("%d/%m/%Y")
df["Hora"] = df["Hora"].astype(str).astype('datetime64[ns]')
df["Hora"] = df["Hora"].dt.strftime("%H:%M")
df['Cant.'] = df['Cant.'].astype(str).astype('float64')
df['Cant.'] = df['Cant.'].astype('int64')
df['Precio'] = df['Precio'].astype(str).astype('float64')
df['Total Venta'] = df['Total Venta'].astype(str).astype('float64')
Estaciones = ["00 SOL", "00 SOL", "00 SOL", "00 SOL", "01 AIRES", "01 AIRES", "01 AIRES", "02 URT", "02 URT", "02 URT", "02 URT", "02 URT", "02 URT"]
df['Estacion'] = Estaciones
del estaciones
df.to_csv("consumo_prueba_resultados", index=False, sep=";")
