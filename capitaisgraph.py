import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/joaombc/APC2021/main/Separado%20por%20Capital.csv")
dados = df.values

'''
dados[:,0]#Aeródromos
dados[:,2]#municipios
dados[:,3]#Jan 2020
dados[:,4]#Jan 2021
dados[:,5]#Variação
'''

t = dados[:,0] + chr(32) + dados[:,2]#Aeródromos + municipios
v = dados[:,3]#Jan 2020
a = dados[:,4]#Jan 2021
b = dados[:,5]#Variação

#Gráfico um começa aqui
barra1 = go.Bar(x = t,
                y = v,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})#barra jan 2020
barra2 = go.Bar(x = t,
                y = a,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})#barra jan 2021

data = [barra1, barra2]#gráfico um terminou

#Gráfico dois começa aqui
linha = go.Scatter(x = t,
                    y = b,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})#linha


pontos = go.Scatter(x = t,
                   y = b,
                   mode = 'markers',
                   name = 'Variação',
                   marker =  {'color' : '#000000',
                              'line' : {'width': 1,
                                        'color': '#000000'}},
                   opacity=.8)#ponto



layout = go.Layout(title = 'Movimento nos Aeródromos das Capitais',
                   xaxis = {'title': 'Aeródromos das Capitais'},
                   yaxis = {'title': 'Movimentação de passageiros'},
                   xaxis_tickangle=-45)



fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

data2 = [linha, pontos]#gráfico dois terminou
layout2 = go.Layout(title = 'Variação nos Aeródromos das Capitais',
                   xaxis = {'title': 'Aeródromos das Capitais'},
                   yaxis = {'title': 'Variação (%)'},
                   xaxis_tickangle=-45)

fig2 = go.Figure(data=data2, layout=layout2)

py.iplot(fig2)