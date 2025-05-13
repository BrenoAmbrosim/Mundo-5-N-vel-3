import pandas as pd
import numpy as np

caminho_arquivo = 'dados.csv'
df = pd.read_csv(caminho_arquivo, sep=';', engine='python', encoding='utf-8')

print(df)

subconjunto_df = df[['ID', 'Date', 'Calories']]
print(subconjunto_df)

pd.set_option('display.max_rows', 9999)
print(df.to_string())

print(df.head(10))
print(df.tail(10))

df.info()
print(df.isnull().sum())
print(df.describe())

df_copia = df.copy()

df_copia['Calories'] = df_copia['Calories'].fillna(0)
print(df_copia)

df_copia['Date'] = df_copia['Date'].fillna('1900/01/01')
print(df_copia)

df_copia['Date'] = df_copia['Date'].replace('1900/01/01', np.nan)

df_copia['Date'] = pd.to_datetime(df_copia['Date'], errors='coerce')

df_copia['Date'] = df_copia['Date'].replace('20201226', '2020/12/26')
df_copia['Date'] = pd.to_datetime(df_copia['Date'], errors='coerce')

df_copia = df_copia.dropna()
print(df_copia)