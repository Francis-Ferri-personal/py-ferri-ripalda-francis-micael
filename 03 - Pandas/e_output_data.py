# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:08:30 2020

@author: franc
"""

# e_output_data.py


import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980: 50519,:].copy()

# Tipos de archivos
# JSON
# Excel
# SQL

# Conexion con Excel
path_excel = "./data/artwork_data.xlsx"
path_excel_no_index = "./data/artwork_data_no_index.xlsx"
path_excel_columns = "./data/artwork_data_columns.xlsx"

sub_df.to_excel(path_excel_no_index, index = False)

columnas = ["artist", "title", "year"]
sub_df.to_excel(path_excel_columns, columns = columnas)


# Multiples hojas de trabajo
path_excel_mt = "./data/artwork_data_mt.xlsx"
writer = pd.ExcelWriter(path_excel_mt, engine = "xlsxwriter")
sub_df.to_excel(writer, sheet_name = "Primera")
sub_df.to_excel(writer, sheet_name = "Segunda")
sub_df.to_excel(writer, sheet_name = "Tercera")
writer.save()

# Formato condicional

path_excel_colores = "./data/artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores, engine = "xlsxwriter")

# Series
num_artistas = sub_df["artist"].value_counts()

print(num_artistas)
print(type(num_artistas))

num_artistas.to_excel(writer, sheet_name = "Artistas")

# Seleccionando la hoj de trabajo
hoja_artistas = writer.sheets["Artistas"]

# Formato

#rango_celdas =  "B2:B{}".format(len(num_artistas.index)+1)

ultimo_numero = (len(num_artistas.index)+1)
rango_celdas = f'B2:B{ultimo_numero}' # B2:B85
rango_celdas_c = f'C2:C{ultimo_numero}' # C2:C85

print(rango_celdas)


formato_artistas = {
    "type": "2_color_scale",
    "min_value": "10",
    "min_type": "percentile",
    "max_value": "99",
    "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)
hoja_artistas.conditional_format(rango_celdas_c, formato_artistas)



# Grafico
workbook  = writer.book
chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'categories': '=Artistas!$A$2:$A$85',
    'values':      '=Artistas!$B$2:$B$85'
})

hoja_artistas.insert_chart('D2', chart)

writer.save()


###### SQL ######
with sqlite3.connect("./data/bdd-artist.bdd") as conexion:
    sub_df.to_sql("py_artistas", conexion)


#with mysql.connect("mysql://user:password@ip:puerto/nombre_base") as conexion:
#    sub_df.to_sql("tabla_mysql", conexion)


###### JSON ######
sub_df.to_json("./data/artistas.json")
sub_df.to_json("./data/artistas_tabla.json", orient = "table")

# Bibliografia
# https://xlsxwriter.readthedocs.io/example_pandas_chart.html

