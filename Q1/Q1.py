import pandas as pd
import os

os.chdir(r'c:\Users\fe092\OneDrive\Área de Trabalho\Samsung\IA\Q1')

df = pd.read_csv('data_studentlist.csv', header='infer')

print("1) Altura média dos estudantes do sexo masculino:", df[df['Gender'] == 'M']['Height'].mean())
print("2) Altura média das estudantes do sexo feminino:", df[df['Gender'] == 'F']['Height'].mean())
print("3) Peso médio dos estudantes do sexo masculino:", df[df['Gender'] == 'M']['Weight'].mean())
print("4) Peso médio das estudantes do sexo feminino:", df[df['Gender'] == 'F']['Weight'].mean())
print("5) Altura do estudante mais alto do sexo masculino:", df[df['Gender'] == 'M']['Height'].max())
print("6) Altura da estudante mais baixa do sexo feminino:", df[df['Gender'] == 'F']['Height'].min())
print("7) Menor peso entre os estudantes de sexo masculino de altura superior a 175cm:", df[(df['Gender'] == 'M') & (df['Height'] > 175)]['Weight'].min())
print("8) Maior peso entre as estudantes de sexo feminino de altura inferior a 160cm:", df[(df['Gender'] == 'F') & (df['Height'] < 160)]['Weight'].max())
print("9) Nota média dos estudantes sem ausência ('N'):", df[df['Absence'] == 'N']['Grade'].mean())
print("10) Nota média dos estudantes com ausência ('Y'):", df[df['Absence'] == 'Y']['Grade'].mean())
print("11) Altura média dos alunos com tipo sanguíneo 'A' ou 'AB':", df[df['Bloodtype'].isin(['A', 'AB'])]['Height'].mean())
print("12) Altura média dos estudantes do sexo masculino com tipo sanguíneo 'A' ou 'AB':", df[(df['Gender'] == 'M') & df['Bloodtype'].isin(['A', 'AB'])]['Height'].mean())
print("13) Idade média dos estudantes com ausência ('Y') cuja nota é igual ou maior que 3:", df[(df['Absence'] == 'Y') & (df['Grade'] >= 3)]['Age'].mean())
