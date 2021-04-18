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

codigo_e_municipio1 = dados2[:,0] + chr(32) + dados2[:,2] # Código ICAO + ascii + Municípios
quantidade_2020_2 = dados2[:,3] # Jan 2020
quantidade_2021_2 = dados2[:,4] # Jan 2021
taxa_de_variacao2 = dados2[:,5] # Variação

regiao = dados3[:,0]#regiao
quantidade_2020_3 = dados3[:,1] # Jan 2020
quantidade_2021_3 = dados3[:,2] # Jan 2021
taxa_de_variacao3 = dados3[:,3] # Variação

'''Gráficos dos estados, capitais e regiões, respectivamente'''

barra_estados_2020 = go.Bar(x = estados,
                y = quantidade_2020_1,
                name = 'Jan/2020',
                marker ={
                        'color' : '#774ef0'
                })

barra_estados_2021 = go.Bar(x = estados,
                  y = quantidade_2021_1,
                  name = 'Jan/2021',
                  marker ={
                           'color' : '#ff4e39'
                  })

linha_variacao_estados = go.Scatter(x = estados,
                    y = taxa_de_variacao1,
                    mode = 'lines',
                    name = '',
                    line ={'color' : '#ee5253',
                            'dash' : 'dash'
                    })

ponto_variacao_estados = go.Scatter(x = estados,
                     y = taxa_de_variacao1,
                     mode = 'markers',
                     name = 'Variação',
                     opacity = .8,
                     marker ={'color' : '#000000',
                              'line' :{'width' : 1,
                                        'color' : '#000000'}
                     })

barra_capitais_2020 = go.Bar(x = codigo_e_municipio1,
                y = quantidade_2020_2,
                name = 'Jan/2020',
                marker ={
                        'color' : '#774ef0'
                })

barra_capitais_2021 = go.Bar(x = codigo_e_municipio1,
                  y = quantidade_2021_2,
                  name = 'Jan/2021',
                  marker ={
                           'color' : '#ff4e39'
                  })

linha_variacao_capitais = go.Scatter(x = codigo_e_municipio1,
                    y = taxa_de_variacao2,
                    mode = 'lines',
                    name = '',
                    line ={'color' : '#ee5253',
                            'dash' : 'dash'
                    })

ponto_variacao_capitais = go.Scatter(x = codigo_e_municipio1,
                     y = taxa_de_variacao2,
                     mode = 'markers',
                     name = 'Variação',
                     opacity = .8,
                     marker ={'color' : '#000000',
                             'line' :{'width' : 1,'color' : '#000000'}
                     })

pie_graph_capitais = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['Jan 2020', 'Jan 2021'])

pie_graph_capitais.add_trace(go.Pie(labels=dados2[:,0] + chr(32) + dados2[:,2], values=dados2[:,3], scalegroup='one',
                     name="Jan 2020"), 1, 1)

pie_graph_capitais.add_trace(go.Pie(labels=dados2[:,0] + chr(32) + dados2[:,2], values=dados2[:,4], scalegroup='two',
                     name="Jan 2021"), 1, 2)

barra_regioes_2020 = go.Bar(x = regiao,
                 y = quantidade_2020_3,
                 name = 'Jan 2020',
                 marker = {'color': '#774ef0'})
barra_regioes_2021 = go.Bar(x = regiao,
                   y = quantidade_2021_3,
                   name = 'Jan 2021',
                   marker = {'color': '#ff4e39'})

linha_variacao_regioes = go.Scatter(x = regiao,
                    y = taxa_de_variacao3,
                    mode = 'lines',
                    name = '',
                    line = {'color': '#ee5253',
                            'dash': 'dash'})

ponto_variacao_regioes = go.Scatter(x = regiao,
                   y = taxa_de_variacao3,
                   mode = 'markers',
                   name = 'Variação',
                   marker =  {'color' : '#000000',
                              'line' : {'width': 1,'color': '#000000'}},
                   opacity=.8)

stack_regioes_2020 = go.Bar(x = regiao,
                y = quantidade_2020_3,
                name = 'Jan 2020',
                marker = {'color': '#774ef0'})

stack_regioes_2021 = go.Bar(x = regiao,
                y = quantidade_2021_3,
                name = 'Jan 2021',
                marker = {'color': '#ff4e39'})

#Estilizando os gráficos
layout_barra_estados = go.Layout(title = 'Movimento dos Estados brasileiros',
                    xaxis ={'title': 'Estados'},
                    yaxis ={'title': 'Movimentação de passageiros'},
                    xaxis_tickangle = -45,
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor = 'rgba(0,0,0,0)')

layout_variacao_estados = go.Layout(title = 'Taxa de variação em cada Estado',
                      xaxis ={'title': 'Estados'},
                      yaxis ={'title' : 'Variação (%)'},
                      xaxis_tickangle = -45,
                      paper_bgcolor = 'rgba(0,0,0,0)',
                      plot_bgcolor = 'rgba(0,0,0,0)')

layout_barra_capital = go.Layout(title = 'Movimento nos aeródromos por Capital',
                    xaxis ={'title': 'Aeródromos das capitais'},
                    yaxis ={'title': 'Movimentação de passageiros'},
                    xaxis_tickangle = -45,
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor = 'rgba(0,0,0,0)')

layout_variacao_capital = go.Layout(title = 'Variação nos aeródromos por Capital',
                      xaxis ={'title': 'Aeródromos das capitais'},
                      yaxis ={'title': 'Variação (%)'},
                      xaxis_tickangle = -45,
                      paper_bgcolor = 'rgba(0,0,0,0)',
                      plot_bgcolor = 'rgba(0,0,0,0)')

layout_barra_regioes = go.Layout(title = 'Movimento das Regiões',
                    xaxis = {'title': 'Regiões'},
                    yaxis = {'title': 'Movimentação de passageiros'},
                    xaxis_tickangle=-45,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')

layout_variacao_regioes = go.Layout(title = 'Variação das Regiões',
                      xaxis = {'title': 'Regiões'},
                      yaxis = {'title': 'Variação (%)'},
                      xaxis_tickangle=-45,
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')

layout_stack_regioes = go.Layout(title = 'Somatório de Jan 2020 & Jan 2021',
                      xaxis = {'title': 'Regiões'},
                      yaxis = {'title': 'Movimentação de passageiros'},
                      barmode = 'stack',
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')

pie_graph_capitais.update_layout(title_text='Porcentagem de voos em Jan 2020 & Jan 2021 para cada Capital')

data_estados_barra = [barra_estados_2020, barra_estados_2021]
data_estados_variacao = [linha_variacao_estados, ponto_variacao_estados]
data_capitais_barra = [barra_capitais_2020, barra_capitais_2021]
data_capitais_variacao = [linha_variacao_capitais, ponto_variacao_capitais]
data_regioes_barra = [barra_regioes_2020,barra_regioes_2021]
data_regioes_variacao = [linha_variacao_regioes, ponto_variacao_regioes]
data_regioes_stack = [stack_regioes_2020, stack_regioes_2021]

fig_barras_estados = go.Figure(data = data_estados_barra, layout = layout_barra_estados)
fig_variacao_estados = go.Figure(data = data_estados_variacao, layout = layout_variacao_estados)
fig_pizza_estados = go.Figure(data=[go.Pie(labels=estados, values= quantidade_2020_1 + quantidade_2021_1)])
fig_pizza_estados.update_layout(title_text='Porcentagem de voos em Jan 2020 + Jan 2021 para cada Estado')
fig_barra_capitais = go.Figure(data = data_capitais_barra,layout = layout_barra_capital)
fig_variacao_capitais = go.Figure(data = data_capitais_variacao, layout = layout_variacao_capital)
fig_barras_regioes = go.Figure(data = data_regioes_barra, layout = layout_barra_regioes)
fig_variacao_regioes = go.Figure(data = data_regioes_variacao, layout = layout_variacao_regioes)
fig_stack_regioes = go.Figure(data = data_regioes_stack,layout = layout_stack_regioes)

pie_graph_capitais.show()
py.iplot(fig_barra_capitais)
py.iplot(fig_variacao_capitais)

fig_pizza_estados.show()
py.iplot(fig_barras_estados)
py.iplot(fig_variacao_estados)

py.iplot(fig_stack_regioes)
py.iplot(fig_barras_regioes)
py.iplot(fig_variacao_regioes)
