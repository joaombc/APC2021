#Biblioptecas importadas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

py.init_notebook_mode(connected=True)

#utilizamos o pandas para abrir o arquivo csv
df = pd.read_csv("https://raw.githubusercontent.com/joaombc/APC2021/main/geral2.csv")

#colocamos os dados dessa tabela em uma lista dentro de uma outra lista
dados = df.values

'''
Os principais valores das colunas dessa lista dentro da lista 
-------> está pegando todos os valores da 1a, 3a, 4a, 5a, 6a coluna, respectivamente.
dados[:,0]#Aeródromos
dados[:,2]#municipios
dados[:,3]#Quantidade de passageiros em Jan 2020
dados[:,4]#Quantidade de passageiros em Jan 2021
dados[:,5]#Variação (%) da quantidade de passageiros
'''

aero_e_municipios = dados[:,0] + chr(32) + dados[:,2]#Aeródromos + municipios
jan_2020 = dados[:,3]#Quantidade de passageiros em Jan 2020
jan_2021 = dados[:,4]#Quantidade de passageiros em Jan 2021
variacao = dados[:,5]#Variação (%) da quantidade de passageiros

#Gráfico um começa aqui
barra_jan_2020 = go.Bar(x = aero_e_municipios,
                y = jan_2020,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})#barra jan 2020
barra_jan_2021 = go.Bar(x = aero_e_municipios,
                y = jan_2021,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})#barra jan 2021

data = [barra_jan_2020, barra_jan_2021]
#Gráfico um terminou

#Gráfico dois começa aqui
linha = go.Scatter(x = aero_e_municipios,
                    y = variacao,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})#linha

pontos = go.Scatter(x = aero_e_municipios,
                   y = variacao,
                   mode = 'markers',
                   name = 'Variação',
                   marker =  {'color' : '#000000',
                              'line' : {'width': 1,
                                        'color': '#000000'}},
                   opacity=.8)#ponto
data2 = [linha, pontos]
#Gráfico dois terminou

#"estilizar" o gráfico 1
layout = go.Layout(title = 'Movimento nos Aeródromos Gerais',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Aeródromos Gerais'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Movimentação de passageiros'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação do aeódromos para melhor visualização

#Imprimir o gráfico 1
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

#"estilizar" o gráfico 2
layout2 = go.Layout(title = 'Variação nos Aeródromos Gerais',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Aeródromos Gerais'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Variação (%)'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação do aeódromos para melhor visualização

#Imprimir o gráfico 2
fig2 = go.Figure(data=data2, layout=layout2)
py.iplot(fig2)