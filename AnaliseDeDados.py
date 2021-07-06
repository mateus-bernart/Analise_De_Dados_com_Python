# Análise de Dados com python

# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# PASSO A PASSO PRA RESOLUÇÃO DE PROBLEMAS
# 
# - Passo 1: importar base de dados.
# - Passo 2: Visualizar a base de dados.
#  - Entender as informações disponíveis
#  - Descobrir as cagadas da base de dados
# - Passo 3: Tratamento da base de dados.
#  - Valores que são números e estão reconhecidos como texto
#  - Valores vazios
# - Passo 4: Análise inicial (exporatória)  -> ver como estão os cancelamentos.
# - Passo 5: Olhar cada característica do cliente e como aquela característica impacta no cancelamento.
# 

# %%
# Passo 1: importar base de dados (pandas)

import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
     

# Passo 3: Tratamento da base de dados
      # Deletar a coluna Unnamed, ela é inútil
tabela = tabela.drop("Unnamed: 0", axis=1) #Eixo 0 é linha, 1 é coluna

display(tabela)


# %%
# As cagadas: 
# Coluna "unnamed" é inútil
# Ver se tem colunas que era pra ser um número e está sendo reconhecida como rexto


#pra transformar uma coluna de texto para número:
tabela["TotalGasto"]= pd.to_numeric(tabela["TotalGasto"], errors="coerce")


# Valor vazio (Nan)
# Colunas completamente vazias
tabela = tabela.dropna(how="all", axis=1) 

# Linhas vazias
tabela = tabela.dropna(how="any", axis=0) # Exclui qualquer valor vazio de linhas

print(tabela.info())


# %%
#Passo 4: Análise inicial (exporatória)  -> ver como estão os cancelamentos.
display(tabela["Churn"].value_counts()) # Conta valor de quantos churns tem na tabela
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #Percentual


# %%
#Passo 5: Olhar cada característica do cliente e como aquela característica impacta no cancelamento.
# Criar gráficos interativos para visualização
import plotly.express as px


for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color= "Churn") #Sempre 3 informações (tabela, valores, cores) )
    grafico.show()
#Sempre que eu fizer um for dentro de uma tabela, ele percorre as colunas da tabela.
#Para linhas: .index

# %% [markdown]
# Conclusões e Ações:
# - Meses como cliente: Número de cancelamentos gigantesco quando o mês está entre o 1º e 2º mês.
#     - Quanto mais tempo o usuário fica com a empresa, menor a chance dele cancelar
#     - Possivelmente a gente tá com um problema de retenção de clientes nos primeiros meses
#     - Ideia: Criar um programa pra incentirvar os clientes nos primeiros meses
#     - Talvez a captação de clientes esteja ruim.
# - Serviço de Internet
#     - Clientes de fibra tem muito mais chance de cancelear.
#     - Provavelmente tem algum problema com a fibra.
#     
# - Quanto mais serviços o cliente tem, menor a chance dele cancelar
#     - Oportunidade gigantesca: temos que criar um programa de incentivo a contratar novos serviços.
#     
# - Serviço de contrato mensal tem muito mais chance de cancelar
#     - Incentivar o cliente pra ir para o contrato anual (desconto, etc)
# - Forma de pagamento: temos que evitar boleto eletrônico, da desconto nas outras alternativas

