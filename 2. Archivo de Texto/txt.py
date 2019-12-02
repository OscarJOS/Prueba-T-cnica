import pandas as pd
import numpy as np
#Ver Nota 2
txt = pd.read_fwf("prueba_txt.txt", widths=[20, 23, 28, 4], encoding='ISO-8859-1', dtype=str, names=["Marca", "Tipo", "Ubicación", "Placa"])
#Agrego la columna Fecha
txt["Fecha"] = "06/07/2019"
#Agrego la columna consecutivo
txt["Consecutivo"] = np.arange(len(txt))
#Guardo el archivo como un CSV sin los indices.
txt.to_csv("prueba_txt", index = False)
