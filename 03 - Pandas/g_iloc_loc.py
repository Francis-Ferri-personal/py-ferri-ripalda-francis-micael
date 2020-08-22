# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:27:48 2020

@author: franc
"""


import pandas as pd

path_guardado = "./data/artwork_data.pickle"
df = pd.read_pickle(path_guardado)

# loc

# Obtenemos toda una fila
filtrado_horizontal = df.loc[1035] #Serie
print(filtrado_horizontal)
print(filtrado_horizontal["artist"])
print(filtrado_horizontal.index) # Indices Columnas
print(filtrado_horizontal.values)

#primero = df.loc[1035, "artist"]
serie_vertical = df["artist"]
print(serie_vertical)
print(serie_vertical.index) # Indices son los indices


# Filtrado potr indice
df_135 = df[df.index == 1035]

# loc -> acceder a un grupo de filas y cilumnas x LAbel (ARR True False)
segundo = df.loc[1035] #FLitar por indicce(o)
segundo = df.loc[[1035,1036]] # Filtar por alregllo de indices

segundo = df.loc[3:5] # filtarndo desde x indice hasta y indice
segundo = df.loc[df.index == 1035] # Arreglo verdaderos y falsos

segundo = df.loc[1035, "artist"] # Un indice
segundo = df.loc[1035, ["artist", "medium"]] # Varios indices


# iloc - acceder a grupo de filas y columnas indices desde 0
tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]
tercero = df.iloc[0:10, 0:4] # Filgtrado indoces Por rango de indice 0:4






