import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir(r'c:\Users\fe092\OneDrive\Área de Trabalho\Samsung\IA\Q4')

df = pd.read_csv('data_coffeeshop.csv', header='infer', na_values=[' '])
df.shape
df.head(5) 

freq_by_year = df['Year of Start'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(freq_by_year.index, freq_by_year.values, marker='o', linestyle='-')
plt.title('Tendência de Abertura de Cafeterias por Ano')
plt.xlabel('Ano')
plt.ylabel('Frequência')
plt.xlim(1997, 2014)
plt.grid(True)
plt.show()

df_in = df[df["Current State"] == "In"]
df_out = df[df["Current State"] == "Out"]

df_in = df_in["Year of Start"].value_counts().sort_index()
df_out = df_out["Year of Start"].value_counts().sort_index()

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlim(1997, 2014)
ax1.plot(df_in.index, df_in.values, marker="o", label="Em operação")
ax1.plot(df_out.index, df_out.values, label="Fora de operação")
ax1.set_title("Quantidade de cafeterias por ano")
ax1.set_xlabel("Ano")
ax1.set_ylabel("Quantidade")
ax1.legend()
plt.show()
