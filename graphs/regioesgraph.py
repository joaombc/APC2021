#Bibliotecas Importadas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

py.init_notebook_mode(connected=True)

#Utilizamos o pandas para abrir o arquivo csv
df = pd.read_csv("https://raw.githubusercontent.com/joaombc/APC2021/main/regioes.csv")

#Colocamos os dados dessa tabela em uma lista dentro de uma outra lista
dados = df.values

'''
Os principais valores das colunas dessa lista dentro da lista 
-------> está pegando todos os valores da 1a, 2a, 2a, 4a coluna, respectivamente.
dados[:,0]#Região
dados[:,1]#Quantidade de passageiros em Jan 2020
dados[:,2]#Quantidade de passageiros em Jan 2021
dados[:,3]#Variação (%) da quantidade de passageiros
'''

regiao = dados[:,0]#Região
jan_2020 = dados[:,1]#Quantidade de passageiros em Jan 2020
jan_2021 = dados[:,2]#Quantidade de passageiros em Jan 2021
variacao = dados[:,3]#Variação (%) da quantidade de passageiros

barra_jan_2020 = go.Bar(x = regiao,
                y = jan_2020,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})#barra jan 2020

barra_jan_2021 = go.Bar(x = regiao,
                y = jan_2021,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})#barra jan 2021

linha = go.Scatter(x = regiao,
                    y = variacao,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})#linha

pontos = go.Scatter(x = regiao,
                   y = variacao,
                   mode = 'markers',
                   name = 'Variação',
                   marker =  {'color' : '#000000',
                              'line' : {'width': 1,
                                        'color': '#000000'}},
                   opacity=.8)#ponto

stack1 = go.Bar(x = regiao,
                y = jan_2020,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})

stack2 = go.Bar(x = regiao,
                y = jan_2021,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})

layout = go.Layout(title = 'Movimento das Regiões',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Regiões'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Movimentação de passageiros'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação do estados para melhor visualização

layout2 = go.Layout(title = 'Variação das Regiões',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Regiões'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Variação da quantidade de passageiros (%)'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação do estados para melhor visualização

layout3 = go.Layout(title = 'Somatório Jan 2020 & Jan 2021',
                   xaxis = {'title': 'Aeródromos'},
                   yaxis = {'title': 'Movimentação de passageiros'},
                   barmode = 'stack')

data = [barra_jan_2020, barra_jan_2021]
data2 = [linha, pontos]
data3 = [stack1, stack2]

fig = go.Figure(data=data, layout=layout)
fig2 = go.Figure(data=data2, layout=layout2)
fig3 = go.Figure(data=data3, layout=layout3)

py.iplot(fig3)
py.iplot(fig)
py.iplot(fig2)