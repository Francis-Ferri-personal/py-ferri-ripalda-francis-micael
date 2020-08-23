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


###########
datos = {
    "nota 1": {
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9},
    "nota 2": {
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9},
    "disciplina": {
        "Pepito": 4,
        "Juanita": 9,
        "Maria": 2}
    }


notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1" ] <= 7
condicion_nota_dos = notas["nota 2" ] <= 7
condicion_disciplina = notas["disciplina"] <= 7

mayores_siete = notas.loc[condicion_nota, ["nota 1"]] # Sigue siendo DataFrame


mayores_siete_df = notas[condicion_nota]["nota 1"] # Se volvio serie

pasaron = notas.loc[condicion_nota][condicion_disciplina]

# Esta logica funciona como un and
pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disciplina]


notas.loc["Maria", "disciplina"] = 7

notas.loc[:, "disciplina"] = 7


###### PROMEDIO DE LAS TRES NOTAS (no1 + no2 + disc /3)

promedio = (notas.loc[:, "nota 1"] + notas.loc[:, "nota 2"] + notas.loc[:, "disciplina"] ) / 3
 