#Biblioptecas importadas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots

py.init_notebook_mode(connected=True)

#utilizamos o pandas para abrir o arquivo csv
df1 = pd.read_csv('https://raw.githubusercontent.com/joaombc/APC2021/main/separado_por_estado.csv')
dados1 = df1.values
df2 = pd.read_csv('https://raw.githubusercontent.com/joaombc/APC2021/main/Separado%20por%20Capital.csv')
dados2 = df2.values
df3 = pd.read_csv('https://raw.githubusercontent.com/joaombc/APC2021/main/regioes.csv')
dados3 = df3.values

''' PLANILHA SEPARADA POR ESTADO
dados1[:,0] # Estado
dados1[:,1] # Jan 2020
dados1[:,2] # Jan 2021
dados1[:,3] # Variação
'''

''' PLANILHA SEPARADA POR CAPITAL
dados2[:,0] # Código ICAO
dados2[:,1] # Aeródromo
dados2[:,2] # Município
dados2[:,3] # Jan 2020
dados2[:,4] # Jan 2021
dados2[:,5] # Variação
'''

''' PLANILHA SEPARADA POR REGIÃO
dados3[:,0] # Região
dados3[:,1] # Jan 2020
dados3[:,2] # Jan 2021
dados3[:,3] # Variação
'''

estados = dados1[:,0] #Estados
quantidade_2020_1 = dados1[:,1] # Jan 2020
quantidade_2021_1 = dados1[:,2] # Jan 2021
taxa_de_variacao1 = dados1[:,3] # Variação

codigo_e_municipio1 = dados2[:,0] + chr(32) + dados2[:,2] # Código ICAO + Municípios
quantidade_2020_2 = dados2[:,3] # Jan 2020
quantidade_2021_2 = dados2[:,4] # Jan 2021
taxa_de_variacao2 = dados2[:,5] # Variação

regiao = dados3[:,0]#regiao
quantidade_2020_3 = dados3[:,1] # Jan 2020
quantidade_2021_3 = dados3[:,2] # Jan 2021
taxa_de_variacao3 = dados3[:,3] # Variação

'''Gráficos dos estados, capitais e regiões, respectivamente'''

barra1 = go.Bar(x = estados,
                y = quantidade_2020_1,
                name = 'Jan/2020',
                marker ={
                        'color' : '#774ef0'
                })

barra1_1 = go.Bar(x = estados,
                  y = quantidade_2021_1,
                  name = 'Jan/2021',
                  marker ={
                           'color' : '#ff4e39'
                  })

linha1 = go.Scatter(x = estados,
                    y = taxa_de_variacao1,
                    mode = 'lines',
                    name = '',
                    line ={'color' : '#ee5253',
                            'dash' : 'dash'
                    })

pontos1 = go.Scatter(x = estados,
                     y = taxa_de_variacao1,
                     mode = 'markers',
                     name = 'Variação',
                     opacity = .8,
                     marker ={'color' : '#000000',
                              'line' :{'width' : 1,
                                        'color' : '#000000'}
                     })

barra2 = go.Bar(x = codigo_e_municipio1,
                y = quantidade_2020_2,
                name = 'Jan/2020',
                marker ={
                        'color' : '#774ef0'
                })

barra2_1 = go.Bar(x = codigo_e_municipio1,
                  y = quantidade_2021_2,
                  name = 'Jan/2021',
                  marker ={
                           'color' : '#ff4e39'
                  })

linha2 = go.Scatter(x = codigo_e_municipio1,
                    y = taxa_de_variacao2,
                    mode = 'lines',
                    name = '',
                    line ={'color' : '#ee5253',
                            'dash' : 'dash'
                    })

pontos2 = go.Scatter(x = codigo_e_municipio1,
                     y = taxa_de_variacao2,
                     mode = 'markers',
                     name = 'Variação',
                     opacity = .8,
                     marker ={'color' : '#000000',
                             'line' :{'width' : 1,'color' : '#000000'}
                     })

sub = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['Jan 2020', 'Jan 2021'])

sub.add_trace(go.Pie(labels=dados2[:,0] + chr(32) + dados2[:,2], values=dados2[:,3], scalegroup='one',
                     name="Jan 2020"), 1, 1)

sub.add_trace(go.Pie(labels=dados2[:,0] + chr(32) + dados2[:,2], values=dados2[:,4], scalegroup='two',
                     name="Jan 2021"), 1, 2)

barra_3 = go.Bar(x = regiao,
                 y = quantidade_2020_3,
                 name = 'Jan 2020',
                 marker = {'color': '#774ef0'})#barra jan 2020
barra_3_1 = go.Bar(x = regiao,
                   y = quantidade_2021_3,
                   name = 'Jan 2021',
                   marker = {'color': '#ff4e39'})#barra jan 2021

linha3 = go.Scatter(x = regiao,
                    y = taxa_de_variacao3,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})#linha

pontos3 = go.Scatter(x = regiao,
                   y = taxa_de_variacao3,
                   mode = 'markers',
                   name = 'Variação',
                   marker =  {'color' : '#000000',
                              'line' : {'width': 1,'color': '#000000'}},
                   opacity=.8)#ponto

stack1 = go.Bar(x = regiao,
                y = quantidade_2020_3,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})

stack2 = go.Bar(x = regiao,
                y = quantidade_2021_3,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})

#Estilizando os gráficos
layout1 = go.Layout(title = 'Movimento dos estados brasileiros',
                    xaxis ={'title': 'Estados'},
                    yaxis ={'title': 'Movimentação de passageiros'},
                    xaxis_tickangle = -45,
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor = 'rgba(0,0,0,0)')

layout1_1 = go.Layout(title = 'Taxa de redução de cada estado',
                      xaxis ={'title': 'Estados'},
                      yaxis ={'title' : 'Variação (%)'},
                      xaxis_tickangle = -45,
                      paper_bgcolor = 'rgba(0,0,0,0)',
                      plot_bgcolor = 'rgba(0,0,0,0)')

layout2 = go.Layout(title = 'Movimento nos aeródromos por capital',
                    xaxis ={'title': 'Aeródromos das capitais'},
                    yaxis ={'title': 'Movimentação de passageiros'},
                    xaxis_tickangle = -45,
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor = 'rgba(0,0,0,0)')

layout2_1 = go.Layout(title = 'Variação nos aeródromos por capital',
                      xaxis ={'title': 'Aeródromos das capitais'},
                      yaxis ={'title': 'Variação (%)'},
                      xaxis_tickangle = -45,
                      paper_bgcolor = 'rgba(0,0,0,0)',
                      plot_bgcolor = 'rgba(0,0,0,0)')

layout3 = go.Layout(title = 'Movimento das Regiões',#Adiciona um título ao gráfico
                    xaxis = {'title': 'Regiões'},#adiciona um 'sentido' a x
                    yaxis = {'title': 'Movimentação de passageiros'},#adiciona um 'sentido' a y
                    xaxis_tickangle=-45,#'angulação do estados para melhor visualização
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')

layout3_1 = go.Layout(title = 'Variação das Regiões',#Adiciona um título ao gráfico
                      xaxis = {'title': 'Regiões'},#adiciona um 'sentido' a x
                      yaxis = {'title': 'Variação (%)'},#adiciona um 'sentido' a y
                      xaxis_tickangle=-45,#'angulação do estados para melhor visualização
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')

layout3_2 = go.Layout(title = 'Somatório de Jan 2020 & Jan 2021',
                      xaxis = {'title': 'Regiões'},
                      yaxis = {'title': 'Movimentação de passageiros'},
                      barmode = 'stack',
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')

sub.update_layout(title_text='Porcentagem de voos em Jan 2020 & Jan 2021 para cada Estado')

data1 = [barra1, barra1_1]
data1_1 = [linha1, pontos1]
data2 = [barra2, barra2_1]
data2_1 = [linha2, pontos2]
data3 = [barra_3,barra_3_1]
data3_1 = [linha3, pontos3]
data3_2 = [stack1, stack2]

fig1 = go.Figure(data = data1,layout = layout1)
fig1_1 = go.Figure(data = data1_1,layout = layout1_1)
fig1_2 = go.Figure(data=[go.Pie(labels=estados, values=quantidade_2020_1 + quantidade_2021_1)])
fig1_2.update_layout(title_text='Porcentagem de voos em Jan 2020 + Jan 2021 para cada Estado')
fig2 = go.Figure(data = data2,layout = layout2)
fig2_1 = go.Figure(data = data2_1,layout = layout2_1)
fig3 = go.Figure(data = data3,layout = layout3)
fig3_1 = go.Figure(data = data3_1,layout = layout3_1)
fig3_2 = go.Figure(data = data3_2,layout = layout3_2)

py.iplot(fig3_2)
py.iplot(fig3)
py.iplot(fig3_1)
fig1_2.show()
py.iplot(fig1)
py.iplot(fig1_1)
sub.show()
py.iplot(fig2)
py.iplot(fig2_1)
