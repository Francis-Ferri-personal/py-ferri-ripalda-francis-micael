# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:15:38 2020

@author: franc
"""


# b_series.py

import numpy as np
import pandas as pd
lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)

series_d = pd.Series([
    True,
    False,
    12,
    12.12,
    "Francis",
    None,
    (1),
    [2],
    {"nombre": "Francis"}])

print(series_d[3])

lista_ciudades = [
    "Ambatoo",
    "Cuenca",
    "Loja",
    "Quito"]

serie_ciudad = pd.Series(
    lista_ciudades,
    index = ["A", 
              "C", 
              "L",
              "Q"])

print(serie_ciudad[3])
print(serie_ciudad["C"])

valores_ciudad = {
    "Ibarra" : 9500,
    "Guayaquil" : 10000,
    "Cuenca": 7000,
    "Quito": 8000,
    "Loja": 3000
    }

serie_valor_ciudad = pd.Series(valores_ciudad)

ciudades_mmenor_5k = serie_valor_ciudad < 5000
print(type(serie_valor_ciudad)) # pandas.core.series.Serie
print(type(ciudades_mmenor_5k)) # pandas.core.series.Serie
print(ciudades_mmenor_5k)

# Este filtro esta buenaso
s5 = serie_valor_ciudad[ciudades_mmenor_5k]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50
print("lima" in serie_valor_ciudad)

svc_cuadrado = np.square(serie_valor_ciudad)

ciudades_uno = pd.Series({
    "montañita": 300,
    "Guayaquil": 10000,
    "Quito": 2000})

ciudades_dos = pd.Series({
    "Loja": 300,
    "Guayaquil": 10000})

ciudades_uno["Loja"] = 0;


# para sumarse debe existir la llave en ambas series,
# Se necesita que las dos series existan

print(ciudades_uno + ciudades_dos)

print(type(ciudades_uno + ciudades_dos))

ciudades_add = ciudades_uno.add(ciudades_dos)

# sub()
# mul()
# div()

ciudades_concat = pd.concat([ciudades_uno, ciudades_dos])


# Sirve para saber si nohay repetidos
# Utiliza True para comprobar si hay repetidos
ciudades_concat_verify = pd.concat([ciudades_uno, ciudades_dos], verify_integrity = False )

ciudades_concat_verify = ciudades_uno.append(ciudades_dos, verify_integrity = False )
print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))


# De mayor a menor
print(ciudades_uno.sort_values(ascending = False).head(2))

# De menor a mayor
print(ciudades_uno.sort_values().tail(2))

# 0 - 1000 5%
# 1001 - 5000 10%
#5001 - 20000 15%

def  calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 1.05
    if (valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    if (valor_serie > 5000):
        return valor_serie * 1.15

ciudad_calculada = ciudades_uno.map(calcular)

# if else
# Cuando NO SE CUMPLE la condicion se aplica
resultado = ciudades_uno.where(ciudades_uno < 1000,
                   ciudades_uno * 1.05)

serie_numeros = pd.Series(["1","1.0", "2", -3])

# integer signed unsigned , float
print(pd.to_numeric(serie_numeros, downcast = "integer"))
serie_numeros_error = pd.Series(["no tiene","1.0", "2", -3])
# ignore, coerce, reise (default)
#print(pd.to_numeric(serie_numeros_error)
print(pd.to_numeric(serie_numeros_error, errors= "ignore"))
print(pd.to_numeric(serie_numeros_error, errors= "coerce"))

      
      
      
      