import pandas as pd

df = pd.read_excel('./aula_13/vendas_eletronicos.xlsx')
print(df)
print('\nFaturamento da empresa: ')
print('\nMáximo: R$ ' + '{:.2f}'.format(df['Faturamento Total (R$)'].max()))
print('Mínimo: R$ ' + '{:.2f}'.format(df['Faturamento Total (R$)'].min()))
print(' Total: R$ ' + '{:.2f}'.format(df['Faturamento Total (R$)'].sum()))
print(' Média: R$ ' + '{:.2f}'.format(df['Faturamento Total (R$)'].mean()))
