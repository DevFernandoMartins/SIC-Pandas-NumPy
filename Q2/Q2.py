import pandas as pd
import numpy as np
import os

os.chdir(r'c:\Users\fe092\OneDrive\Área de Trabalho\Samsung\IA\Q2')

df = pd.read_csv('data_census.csv', header='infer')
df.shape
df.head(10) 
df['Population'] = df['Population'].str.replace(',', '', regex=True).str.strip()
df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
df['Households'] = df['Households'].str.replace(',', '', regex=True).str.strip()
df['Households'] = pd.to_numeric(df['Households'], errors='coerce')


print("1) Qual é a população total onde a variável ProvinceCode seja igual a 115 ou 116: ", df[df['Province Code'].isin([115, 116])]['Population'].sum())
print("2) Qual é a população média das cidades onde há mais homens: ", df[df['Gender Ratio'] > 1]['Population'].mean())
print("3) Quais são os lugares com mais homens (GenderRatio >1) e menos de 2 pessoas por domicílio (household): \n", df[(df['Gender Ratio'] > 1) & (df['Households'] < 2)])
print("4) Ordenar o DataFrame por ordem ascendente dos domincílios (Households). Mostrar os 10 primeiros: \n", df.sort_values(by='Households', ascending=True).head(10))
