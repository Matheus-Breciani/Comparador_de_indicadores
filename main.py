#1 - importar a base de dados
import pandas as pd
tabela = pd.read_csv("D:\Intensivão Python\AULA 2/telecom.dados.csv")

#2 - visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)

#3 - tratamento de dados
# - valores reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - valores vazios
#deletando colunas vazias
tabela = tabela.dropna(how="all", axis=1)

#deletando linhas vazias
tabela = tabela.dropna(how="any", axis=0)

#print(tabela.info())

#4  Análise inicial
#como estão nosso cancelamentos?
#print(tabela["Churn"].value_counts())


#5 - Análise completa
#comparar cada coluna da tabela com a coluna de cancelamneto
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()