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
                   y = b,#Bibliotecas Importadas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

py.init_notebook_mode(connected=True)

#Utilizamos o pandas para abrir o arquivo csv
df = pd.read_csv("https://raw.githubusercontent.com/joaombc/APC2021/main/Separado%20por%20Capital.csv")


#Colocamos os dados dessa tabela em uma lista dentro de uma outra lista
dados = df.values

'''
dados[:,0]#Aeródromos
dados[:,2]#municipios
dados[:,3]#Quantidade de passageiros em Jan 2020
dados[:,4]#Quantidade de passageiros em Jan 2021
dados[:,5]#Variação (%) da quantidade de passageiros
'''

capitais = dados[:,0] + chr(32) + dados[:,2]#Aeródromos + municipios
jan_2020 = dados[:,3]#Quantidade de passageiros em Jan 2020
jan_2021 = dados[:,4]#Quantidade de passageiros em Jan 2021
variacao = dados[:,5]#Variação (%) da quantidade de passageiros

#Gráfico um começa aqui
barra_jan_2020 = go.Bar(x = capitais,
                y = jan_2020,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})#barra jan 2020
barra_jan_2021 = go.Bar(x = capitais,
                y = jan_2021,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})#barra jan 2021

data = [barra_jan_2020, barra_jan_2021]
#Gráfico um terminou

#Gráfico dois começa aqui
linha = go.Scatter(x = capitais,
                    y = variacao,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})#linha
pontos = go.Scatter(x = capitais,
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
layout = go.Layout(title = 'Movimento nos Aeródromos das Capitais',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Aeródromos das Capitais'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Movimentação de passageiros'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação dos aeódromos para melhor visualização

#Imprimir o gráfico 1
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

#"estilizar" o gráfico 2
layout2 = go.Layout(title = 'Variação nos Aeródromos das Capitais',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Aeródromos das Capitais'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Variação (%)'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação dos aeódromos para melhor visualização

#Imprimir o gráfico 1
fig2 = go.Figure(data=data2, layout=layout2)
py.iplot(fig2)
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
