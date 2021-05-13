import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

app = dash.Dash(__name__, suppress_callback_exceptions=True,meta_tags=[{'name': 'viewport', 'content': 'width = device-width, initial-scale = 1'}])

app.config.suppress_callback_exceptions = True
server = app.server
app_color = {'graph_bg': '#082255', 'graph_line': '#007ACE'}
fig_plot = html.Div(id='fig_plot')
df1 = pd.read_csv('https://raw.githubusercontent.com/joaombc/APC2021/main/separado_por_estado.csv')
dados1 = df1.values
df2 = pd.read_csv('https://raw.githubusercontent.com/joaombc/APC2021/main/Separado%20por%20Capital.csv')
dados2 = df2.values

from urllib.request import urlopen
with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:Brazil = json.load(response)

sudeste = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
norte = ['Pará', 'Amazonas', 'Rondônia', 'Amapá', 'Tocantins', 'Acre', 'Roraima']
nordeste = ['Bahia', 'Pernambuco', 'Ceará', 'Rio Grande do Norte', 'Alagoas', 'Maranhão', 'Paraíba', 'Sergipe', 'Piauí']
sul = ['Rio Grande do Sul', 'Paraná', 'Santa Catarina']
centrooeste = ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul']
sd_2020 = 0
sd_2021 = 0
ne_2020 = 0
ne_2021 = 0
no_2020 = 0
no_2021 = 0
sul_2020 = 0
sul_2021 = 0
co_2020 = 0
co_2021 = 0

for linha in dados1:
    if linha[0] in sudeste:
        sd_2020 += linha[1]
        sd_2021 += linha[2]
    elif linha[0] in nordeste:
        ne_2020 += linha[1]
        ne_2021 += linha[2]
    elif linha[0] in norte:
        no_2020 += linha[1]
        no_2021 += linha[2]
    elif linha[0] in sul:
        sul_2020 += linha[1]
        sul_2021 += linha[2]
    elif linha[0] in centrooeste:
        co_2020 += linha[1]
        co_2021 += linha[2]

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

estados = dados1[:, 0]  # Estados
quantidade_2020_1 = dados1[:, 1]  # Jan 2020
quantidade_2021_1 = dados1[:, 2]  # Jan 2021
taxa_de_variacao1 = dados1[:, 3]  # Variação

codigo_e_municipio1 = dados2[:, 0] + chr(32) + dados2[:, 2]  # Código ICAO + Municípios
quantidade_2020_2 = dados2[:, 3]  # Jan 2020
quantidade_2021_2 = dados2[:, 4]  # Jan 2021
taxa_de_variacao2 = dados2[:, 5]  # Variação

regioes = ['Sudeste', 'Nordeste', 'Sul', 'Centro-Oeste', 'Norte']
reg_2020 = [sd_2020, ne_2020, sul_2020, co_2020, no_2020]
reg_2021 = [sd_2021, ne_2021, sul_2021, co_2021, no_2021]
reg_variacao = [round(100 * (sd_2021 / sd_2020) - 100, 2),
                round(100 * (ne_2021 / ne_2020) - 100, 2),
                round(100 * (sul_2021 / sul_2020) - 100, 2),
                round(100 * (co_2021 / co_2020) - 100, 2),
                round(100 * (no_2021 / no_2020) - 100, 2)]

barra_estados_2020 = go.Bar(x=estados,
                            y=quantidade_2020_1,
                            name='Jan/2020',
                            marker={'color': '#774ef0'})

barra_estados_2021 = go.Bar(x=estados,
                            y=quantidade_2021_1,
                            name='Jan/2021',
                            marker={'color': '#ff4e39'})

linha_variacao_estados = go.Scatter(x=estados,
                                    y=taxa_de_variacao1,
                                    mode='lines',
                                    name='',
                                    line={'color': '#ee5253',
                                        'dash': 'dash'})

ponto_variacao_estados = go.Scatter(x=estados,
                                    y=taxa_de_variacao1,
                                    mode='markers',
                                    name='Variação',
                                    opacity=.8,
                                    marker={'color': '#000000',
                                        'line':{'width': 1,
                                                'color': '#000000'}})

barra_capitais_2020 = go.Bar(x=codigo_e_municipio1,
                             y=quantidade_2020_2,
                             name='Jan/2020',
                             marker={'color': '#774ef0'})

barra_capitais_2021 = go.Bar(x=codigo_e_municipio1,
                             y=quantidade_2021_2,
                             name='Jan/2021',
                             marker={'color': '#ff4e39'})

linha_variacao_capitais = go.Scatter(x=codigo_e_municipio1,
                                     y=taxa_de_variacao2,
                                     mode='lines',
                                     name='',
                                     line={'color': '#ee5253',
                                         'dash': 'dash'})

ponto_variacao_capitais = go.Scatter(x=codigo_e_municipio1,
                                     y=taxa_de_variacao2,
                                     mode='markers',
                                     name='Variação',
                                     opacity=.8,
                                     marker={'color': '#000000',
                                         'line':{
                                                 'width': 1,
                                                 'color': '#000000' }})

pie_graph_capitais = make_subplots(1, 2,specs= [[{'type': 'domain'},{'type': 'domain'}]],subplot_titles=['Jan 2020', 'Jan 2021'])

pie_graph_capitais.add_trace(go.Pie(labels=dados2[:, 0] + chr(32) + dados2[:, 2],values=dados2[:, 3],scalegroup='one',
                                name='Jan 2020',hovertemplate='%{label} <br>Variação: %{percent} </br>%{name}'), 1, 1)

pie_graph_capitais.add_trace(go.Pie(labels=dados2[:, 0] + chr(32) + dados2[:, 2],values=dados2[:, 4],scalegroup='one',
                                    name='Jan 2021', hovertemplate='%{label} <br>Variação: %{percent} </br>%{name}'), 1,2)

barra_regioes_2020 = go.Bar(x=regioes,
                            y=reg_2020,
                            name='Jan/2020',
                            marker={ 'color': '#774ef0'})

barra_regioes_2021 = go.Bar(x=regioes,
                            y=reg_2021,
                            name='Jan/2021',
                            marker={'color': '#ff4e39'})

linha_variacao_regioes = go.Scatter(x=regioes,
                                    y=reg_variacao,
                                    mode='lines',
                                    name='',
                                    line={'color': '#ee5253',
                                        'dash': 'dash'})

ponto_variacao_regioes = go.Scatter(x=regioes,
                                    y=reg_variacao,
                                    mode='markers',
                                    name='Variação',
                                    marker={'color': '#000000',
                                            'line':{'width': 1,'color': '#000000'}},
                                    opacity=.8)

stack_regioes_2020 = go.Bar(x=regioes,
                            y=reg_2020,
                            name='Jan/2020',
                            marker={'color': '#774ef0'})

stack_regioes_2021 = go.Bar(x=regioes,
                            y=reg_2021,
                            name='Jan/2021',
                            marker={'color': '#ff4e39'})

pie_graph_regioes = make_subplots(1, 2,specs=[[{'type': 'domain'},{'type': 'domain'}]],subplot_titles=['Jan 2020','Jan 2021'])

pie_graph_regioes.add_trace(go.Pie(labels=regioes,values=reg_2020,scalegroup='one',name='Jan 2020'), 1, 1)

pie_graph_regioes.add_trace(go.Pie(labels=regioes,values=reg_2021,scalegroup='two',name='Jan 2021'), 1, 2)

mapa_estados_2020 = px.choropleth(df1,
                                geojson=Brazil,
                                featureidkey='properties.name',
                                locations='Estado',
                                color='Jan 2020',
                                color_continuous_scale=['#774ef0','#ff4e39'],
                                hover_name='Estado',
                                hover_data=['Jan 2020','Taxa de crescimento (%)'])

mapa_estados_2021 = px.choropleth(df1,
                                geojson=Brazil,
                                featureidkey='properties.name',
                                locations='Estado',
                                color='Jan 2021',
                                color_continuous_scale=['#774ef0','#ff4e39'],
                                hover_name='Estado',
                                hover_data=['Jan 2021','Taxa de crescimento (%)'])

mapa_estados_2020.update_geos(fitbounds='locations',
                              visible=False,
                              bgcolor='rgba(0,0,0,0)',
                              resolution=110,
                              showcoastlines=True,
                              coastlinecolor='RebeccaPurple',
                              showocean=True,
                              oceancolor='LightBlue')

mapa_estados_2021.update_geos(fitbounds='locations',
                              visible=False,
                              bgcolor='rgba(0,0,0,0)',
                              resolution=110,
                              showcoastlines=True,
                              coastlinecolor='RebeccaPurple',
                              showocean=True,
                              oceancolor='LightBlue')

mapa_estados_2020.update_layout(legend=dict(font=dict(color='white')),
                                font=dict(color='white'),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)', )

mapa_estados_2021.update_layout(legend=dict(font=dict(color='white')),
                                font=dict(color='white'),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)', )

layout_barra_capital = go.Layout(xaxis={'color': 'white'},
                                yaxis={'title': 'Movimentação de passageiros','color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                xaxis_tickangle=-45,
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                legend=dict(yanchor='top',y=1,xanchor='left',x=0.90,font=dict(color='white')))

layout_variacao_capital = go.Layout(xaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                    yaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                    xaxis_tickangle=-45,
                                    paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False)

layout_barra_regioes = go.Layout(xaxis={'color': 'white'},
                                yaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                xaxis_tickangle=-45,
                                paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
                                legend=dict(yanchor='top',y=1,xanchor='left',x=0.90,font=dict(color='white')))

layout_variacao_regioes = go.Layout(xaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                    yaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                    xaxis_tickangle=-45,
                                    paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False)

layout_stack_regioes = go.Layout(go.Layout(xaxis={'color': 'white'},
                                yaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                xaxis_tickangle=-45,
                                paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
                                legend=dict(yanchor='top',y=1,xanchor='left',x=0.90,font=dict(color='white'))))

data_estados_barra = [barra_estados_2020, barra_estados_2021]
data_estados_variacao = [linha_variacao_estados, ponto_variacao_estados]
data_capitais_barra = [barra_capitais_2020, barra_capitais_2021]
data_capitais_variacao = [linha_variacao_capitais, ponto_variacao_capitais]
data_regioes_barra = [barra_regioes_2020, barra_regioes_2021]
data_regioes_variacao = [linha_variacao_regioes, ponto_variacao_regioes]
data_regioes_stack = [stack_regioes_2020, stack_regioes_2021]
fig_pizza_estados2020 = go.Figure(data=[go.Pie(labels=estados, values=quantidade_2020_1)])
fig_pizza_estados2020.update_layout(legend=dict(font=dict(color='white')),
                                    font=dict(color='white'),
                                    paper_bgcolor='rgba(0,0,0,0)',
                                    plot_bgcolor='rgba(0,0,0,0)')

fig_pizza_estados2021 = go.Figure(data=[go.Pie(labels=estados, values=quantidade_2021_1)])
fig_pizza_estados2021.update_layout(legend=dict(font=dict(color='white')),
                                    font=dict(color='white'),
                                    paper_bgcolor='rgba(0,0,0,0)',
                                    plot_bgcolor='rgba(0,0,0,0)')

fig_barra_capitais = go.Figure(data=data_capitais_barra, layout=layout_barra_capital)
fig_variacao_capitais = go.Figure(data=data_capitais_variacao, layout=layout_variacao_capital)
fig_pie_capitais = go.Figure(data=pie_graph_capitais)
fig_pie_capitais.update_layout(legend=dict(font=dict(color='white')),
                                            font=dict(color='white'),
                                            paper_bgcolor='rgba(0,0,0,0)',
                                            plot_bgcolor='rgba(0,0,0,0)')

fig_pie_capitais_2020 = go.Figure(data=[go.Pie(labels=codigo_e_municipio1, values=dados2[:, 3])])
fig_pie_capitais_2020.update_layout(legend=dict(yanchor='top',y=1,xanchor='left', x=1.50,
                                    font=dict(color='white')),font=dict(color='white'),margin=dict(t=0, b=0, l=0, r=0),
                                    paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False)

fig_pie_capitais_2021 = go.Figure(data=[go.Pie(labels=codigo_e_municipio1, values=dados2[:, 4])])

fig_pie_capitais_2021.update_layout(legend=dict(yanchor='top',y=1,xanchor='left', x=1.50,
                                    font=dict(color='white')),font=dict(color='white'),margin=dict(t=0, b=0, l=0, r=0),
                                    paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False)

fig_barras_regioes = go.Figure(data=data_regioes_barra, layout=layout_barra_regioes)
fig_variacao_regioes = go.Figure(data=data_regioes_variacao, layout=layout_variacao_regioes)
fig_stack_regioes = go.Figure(data=data_regioes_stack, layout=layout_stack_regioes)
fig_pie_regioes = go.Figure(data=pie_graph_regioes)

fig_pie_regioes.update_layout(legend=dict(yanchor='top',y=1,xanchor='left',x=-0.10,
                                            font=dict(color='white')),font=dict(color='white'),
                                            paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

tabs_styles = {
    'height': '44px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

pagina1 = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H6('MOVIMENTO DOS ESTADOS BRASILEIROS',
                                className='graph__title')
                    ]
                ),
                html.Br(),
                dcc.Dropdown(
                    id='teste-filtro',
                    options=
                    [
                        {
                            'label': nome,
                            'value': nome
                        } for nome in regioes
                    ],
                    value=regioes[0],
                    clearable=False,
                    style=
                    {
                        'width': '70%'
                    }
                ),
                dcc.Graph(id='teste'),
                html.Br(),
                html.Div(
                    [
                        html.H6('TAXA DE VARIAÇÃO ENTRE CADA ESTADO',
                                className='graph__title')
                    ]
                ),
                dcc.Graph(id='teste2'),
            ],
            className='two-thirds column wind__speed__container',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6('DIFERENÇA ENTRE ESTADOS EM 2020',
                                        className='graph__title')
                            ]
                        ),
                        dcc.Graph(figure=mapa_estados_2020),
                    ],
                    className='graph__container first',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6('DIFERENÇA ENTRE ESTADOS EM 2021',
                                        className='graph__title')
                            ]
                        ),
                        dcc.Graph(figure=mapa_estados_2021),
                    ],
                    className='graph__container second',
                ),
            ],
            className='one-third column histogram__direction',
        ),
    ],
    className='app__content',
)

pagina2 = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H6('MOVIMENTO NOS AERÓDROMOS POR CAPITAL',
                                className='graph__title')
                    ]
                ),
                dcc.Graph(figure=fig_barra_capitais),
                html.Br(),
                html.Div(
                    [
                        html.H6('VARIAÇÃO DE VOOS ENTRE JAN 2020 & JAN 2021',
                                className='graph__title')
                    ]
                ),
                dcc.Graph(figure=fig_variacao_capitais),
            ],
            className='two-thirds column wind__speed__container',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6('PORCENTAGEM DE VOOS POR CAPITAL EM JAN 2020',
                                        className='graph__title')
                            ]
                        ),
                        dcc.Graph(figure=fig_pie_capitais_2020),
                    ],
                    className='graph__container first',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6('PORCENTAGEM DE VOOS POR CAPITAL EM JAN 2021',
                                        className='graph__title')
                            ]
                        ),
                        dcc.Graph(figure=fig_pie_capitais_2021),
                    ],
                    className='graph__container second',
                ),
            ],
            className='one-third column histogram__direction',
        ),
    ],
    className='app__content',
)

pagina3 = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H6('MOVIMENTO DAS REGIÕES',
                                className='graph__title')
                    ]
                ),
                dcc.Graph(figure=fig_barras_regioes),
                html.Br(),
                html.Div(
                    [
                        html.H6('PORCENTAGEM DE PASSAGEIROS POR REGIÃO',
                                className='graph__title')
                    ]
                ),
                dcc.Graph(figure=fig_pie_regioes),
            ],
            className='two-thirds column wind__speed__container',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6('SOMATÓRIO DE JAN 2020 & JAN 2021',
                                        className='graph__title')
                            ]
                        ),
                        dcc.Graph(figure=fig_stack_regioes),
                    ],
                    className='graph__container first',
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6('VARIAÇÃO DAS REGIÕES',
                                        className='graph__title')
                            ]
                        ),
                        dcc.Graph(figure=fig_variacao_regioes),
                    ],
                    className='graph__container second',
                ),
            ],
            className='one-third column histogram__direction',
        ),
    ],
    className='app__content',
)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H4('MOVIMENTAÇÃO DE PASSAGEIROS',
                                className='app__header__title'),
                        html.P('Comparação da movimentação de passageiros entre os períodos Jan/2020 e Jan/2021.',
                               className="app__header__title--grey"),
                    ],
                    className='app__header__desc',
                ),
                html.Div(
                    [
                        html.Img(src=app.get_asset_url('dash-new-logo.png'),
                                 className='app__menu__img')
                    ],
                    className='app__header__logo',
                ),
            ],
            className='app__header',
        ),
        dcc.Tabs(
            id='grafico_selecionado',
            children=
            [
                dcc.Tab(label='Estados', value='tab-1', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Capitais', value='tab-2', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Regiões', value='tab-3', style=tab_style, selected_style=tab_selected_style),
            ],
            value='tab-1',
            className='form-tabs',
        ),
        fig_plot,
    ],
    className='app__container',
)

@app.callback(Output('fig_plot', 'children'),
            [Input('grafico_selecionado', 'value')])

def grafico_escolhido(value):
    if value == 'tab-1':
        return pagina1
    elif value == 'tab-2':
        return pagina2
    elif value == 'tab-3':
        return pagina3

@app.callback(Output('teste', 'figure'),
             [Input('teste-filtro', 'value')])

def gera_barras(regiao):
    if regiao == 'Sudeste':
        estados_escolhido = sudeste
    if regiao == 'Nordeste':
        estados_escolhido = nordeste
    if regiao == 'Sul':
        estados_escolhido = sul
    if regiao == 'Centro-Oeste':
        estados_escolhido = centrooeste
    if regiao == 'Norte':
        estados_escolhido = norte

    quan2020 = []
    quan2021 = []

    for estado, quanti_20, quanti_21 in zip(estados, quantidade_2020_1, quantidade_2021_1):
        for escolhido in estados_escolhido:
            if escolhido == estado:
                quan2020.append(quanti_20)
                quan2021.append(quanti_21)

    barra_estados_2020 = go.Bar(x=estados_escolhido,
                                y=quan2020,
                                name='Jan/2020',
                                marker={'color': '#774ef0'})

    barra_estados_2021 = go.Bar(x=estados_escolhido,
                                y=quan2021,
                                name='Jan/2021',
                                marker={'color': '#ff4e39'})

    data_estados_barra = [barra_estados_2020, barra_estados_2021]

    layout_barra_estados = go.Layout(xaxis={'color': 'white'},
                                    yaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                    xaxis_tickangle=-45,
                                    paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
                                    legend=dict(yanchor='top', y=1, xanchor='left', x=0.90, font=dict(color='white')))

    fig_barras_estados = go.Figure(data=data_estados_barra, layout=layout_barra_estados)
    return fig_barras_estados

@app.callback(
    Output('teste2', 'figure'),
    [Input('teste-filtro', 'value')])

def gera_variacao(regiao):
    if regiao == 'Sudeste':
        estados_escolhido = sudeste
    if regiao == 'Nordeste':
        estados_escolhido = nordeste
    if regiao == 'Sul':
        estados_escolhido = sul
    if regiao == 'Centro-Oeste':
        estados_escolhido = centrooeste
    if regiao == 'Norte':
        estados_escolhido = norte

    taxavar = []

    for estado, taxa in zip(estados, taxa_de_variacao1):
        for escolhido in estados_escolhido:
            if escolhido == estado:
                taxavar.append(taxa)

    linha_variacao_estados = go.Scatter(x=estados_escolhido,
                                        y=taxavar,
                                        mode='lines',
                                        name='',
                                        line={'color': '#ee5253',
                                            'dash': 'dash'})

    ponto_variacao_estados = go.Scatter(x=estados_escolhido,
                                        y=taxavar,
                                        mode='markers',
                                        name='Variação',
                                        opacity=.8,
                                        marker={'color': '#000000',
                                                'line':{'width': 1,'color': '#000000'}})

    data_estados_variacao = [linha_variacao_estados, ponto_variacao_estados]

    layout_variacao_estados = go.Layout(xaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                        yaxis={'color': 'white','showgrid': False,'showline': False,'fixedrange': True,'zeroline': True},
                                        xaxis_tickangle=-45,
                                        paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',showlegend=False)

    fig_variacao_estados = go.Figure(data=data_estados_variacao, layout=layout_variacao_estados)
    return fig_variacao_estados

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)
