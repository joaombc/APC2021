#Bibliotecas Importadas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

py.init_notebook_mode(connected=True)

#Utilizamos o pandas para abrir o arquivo csv
df = pd.read_csv("https://raw.githubusercontent.com/joaombc/APC2021/main/separado_por_estado.csv")


#Colocamos os dados dessa tabela em uma lista dentro de uma outra lista
dados = df.values

'''
Os principais valores das colunas dessa lista dentro da lista 
-------> está pegando todos os valores da 1a, 2a, 2a, 4a coluna, respectivamente.
dados[:,0]#Estados
dados[:,1]#Quantidade de passageiros em Jan 2020
dados[:,2]#Quantidade de passageiros em Jan 2021
dados[:,3]#Variação (%) da quantidade de passageiros
'''

estados = dados[:,0]#Estados
jan_2020 = dados[:,1]#Quantidade de passageiros em Jan 2020
jan_2021 = dados[:,2]#Quantidade de passageiros em Jan 2021
variacao = dados[:,3]#Variação (%) da quantidade de passageiros

#Gráfico um começa aqui
barra_jan_2020 = go.Bar(x = estados,
                y = jan_2020,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})#barra jan 2020
barra_jan_2021 = go.Bar(x = estados,
                y = jan_2021,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})#barra jan 2021

data = [barra_jan_2020, barra_jan_2021]
#Gráfico um terminou

#Gráfico dois começa aqui
linha = go.Scatter(x = estados,
                    y = variacao,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})#linha
pontos = go.Scatter(x = estados,
                   y = variacao,
                   mode = 'markers',
                   name = 'Variação',
                   marker =  {'color' : '#000000',
                              'line' : {'width': 1,
                                        'color': '#000000'}},
                   opacity=.8)#ponto

data2 = [linha, pontos]#gráfico dois terminou

#"estilizar" o gráfico 1
layout = go.Layout(title = 'Movimento dos Estados',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Estados'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Movimentação de passageiros'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação do estados para melhor visualização

#Imprimir o gráfico 1
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

#"estilizar" o gráfico 2
layout2 = go.Layout(title = 'Variação nos Estados',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Estados'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Variação da quantidade de passageiros (%)'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação do estados para melhor visualização

#Imprimir o gráfico 2
fig2 = go.Figure(data=data2, layout=layout2)
py.iplot(fig2)
