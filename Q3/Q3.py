import pandas as pd
import numpy as np
import os

os.chdir(r'c:\Users\fe092\OneDrive\Área de Trabalho\Samsung\IA\Q3')

df = pd.read_csv('data_sales.csv', header='infer')
df.shape
df.head(10) 

df['Amount'] = df['Unit Price'] * df['Units']

print("2) Preço unitário médio para cada região (usando groupby()):")
print(df.groupby('Region')['Unit Price'].mean())

print("\n3) Preço unitário médio para cada região (usando pivot_table()):")
print(df.pivot_table(values='Unit Price', index='Region', aggfunc='mean'))

print("\n4) Preço unitário médio e unidades para cada região (usando groupby()):")
print(df.groupby('Region').agg({'Unit Price': 'mean', 'Units': 'sum'}))

print("\n5) Preço unitário médio e unidades para cada região (usando pivot_table()):")
print(df.pivot_table(values=['Unit Price', 'Units'], index='Region', aggfunc={'Unit Price': 'mean', 'Units': 'sum'}))

print("\n6) Total de unidades por região e tipo de item (usando pivot_table()):")
print(df.pivot_table(values='Units', index=['Region', 'Item'], aggfunc='sum', fill_value=0))

print("\n7) Valor total de vendas por região e tipo de item (usando pivot_table()):")
print(df.pivot_table(values='Amount', index=['Region', 'Item'], aggfunc='sum', fill_value=0))