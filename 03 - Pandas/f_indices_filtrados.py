# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:09:00 2020

@author: franc
"""


import pandas as pd

ArithmeticError(args)path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)
serie_artistas_duplicados = df["artist"]

artistas = pd.unique(serie_artistas_duplicados)
print(type(artistas)) # numpy array

print(artistas.size)

blake = df["artist"] == "Blake, William" # Serie


print(blake.value_counts())


df_blake = df[blake] # Dataframe



