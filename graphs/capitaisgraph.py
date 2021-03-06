#Bibliotecas Importadas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots

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

barra_jan_2020 = go.Bar(x = capitais,
                y = jan_2020,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})#barra jan 2020
barra_jan_2021 = go.Bar(x = capitais,
                y = jan_2021,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})#barra jan 2021

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

fig3 = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['Jan 2020', 'Jan 2021'])
fig3.add_trace(go.Pie(labels=capitais, values=dados[:,3], scalegroup='one',
                     name="Jan 2020"), 1, 1)
fig3.add_trace(go.Pie(labels=capitais, values=dados[:,4], scalegroup='one',
                     name="Jan 2021"), 1, 2)

layout = go.Layout(title = 'Movimento nos Aeródromos das Capitais',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Aeródromos das Capitais'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Movimentação de passageiros'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação dos aeódromos para melhor visualização

layout2 = go.Layout(title = 'Variação nos Aeródromos das Capitais',#Adiciona um título ao gráfico
                   xaxis = {'title': 'Aeródromos das Capitais'},#adiciona um 'sentido' a x
                   yaxis = {'title': 'Variação da quantidade de passageiros (%)'},#adiciona um 'sentido' a y
                   xaxis_tickangle=-45)#'angulação dos aeódromos para melhor visualização

fig3.update_layout(title_text='Porcentagem de voos em Jan 2020 & Jan 2021')

data = [barra_jan_2020, barra_jan_2021]
data2 = [linha, pontos]

fig = go.Figure(data=data, layout=layout)
fig2 = go.Figure(data=data2, layout=layout2)

fig3.show()
py.iplot(fig)
py.iplot(fig2)