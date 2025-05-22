import pandas as pd

data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 25, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.79, 1.80, 1.75]
    }

df_dados = pd.DataFrame(data)
print(df_dados)

print('\nVariáveis Quantitativas')

print('Exibir Idade: ')
print(df_dados['Idade'])

print('Exibir Altura: ')
print(df_dados['Altura'])

print('\nVariáveis Qualitativas')

print('Exibir Nome: ')
print(df_dados['Nome'])

print('Exibir Gênero: ')
print(df_dados['Gênero'])
