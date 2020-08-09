# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:42:59 2020

@author: franc
"""
# d_lectura_csv-py

# 03_pandas
#   d_lectutra_csv.py
#   data
#      artwork.csv

import pandas as pd
import os
path = "./data/artwork_data.csv"

df1 = pd.read_csv(
    path, 
    nrows = 10)

columnas = ["id","artist","title","medium","year","acquisitionYear","width","height","units" ]
df2 = pd.read_csv(path, nrows = 10, usecols = columnas)
df3 = pd.read_csv(path, 
                  #nrows = 10,
                  usecols = columnas,
                  index_col = "id")
path_guardado = "./data/artwork_data.pickle"

df3.to_pickle(path_guardado)