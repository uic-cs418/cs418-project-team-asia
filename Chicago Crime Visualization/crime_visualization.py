import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


df = pd.read_csv("Crimes_-_2001_to_present .csv")
df = df[(df.Year != 2011) & (df.Year != 2019)]

year2012 = len(df[df.Year == 2012])
year2013 = len(df[df.Year == 2013])
year2014 = len(df[df.Year == 2014])
year2015 = len(df[df.Year == 2015])
year2016 = len(df[df.Year == 2016])
year2017 = len(df[df.Year == 2017])
year2018 = len(df[df.Year == 2018])

arrest = df[(df.Arrest == 1)].groupby(['Year'])[['ID']].count().reset_index()
notarrest = df[(df.Arrest == 0)].groupby(['Year'])[['ID']].count().reset_index()

df2012 = df[(df.Year == 2012)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2013 = df[(df.Year == 2013)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2014 = df[(df.Year == 2014)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2015 = df[(df.Year == 2015)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2016 = df[(df.Year == 2016)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2017 = df[(df.Year == 2017)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2018 = df[(df.Year == 2018)].groupby(['Primary Type'])[['ID']].count().reset_index()

theftArrest = df[(df.Arrest == 1) & (df['Primary Type'] == 'THEFT')].groupby(['Year'])[['ID']].count().reset_index()
theftNotArrest = df[(df.Arrest == 0) & (df['Primary Type'] == 'THEFT')].groupby(['Year'])[['ID']].count().reset_index()
homicideArrest = df[(df.Arrest == 1) & (df['Primary Type'] == 'HOMICIDE')].groupby(['Year'])[['ID']].count().reset_index()
homicideNotArrest = df[(df.Arrest == 0) & (df['Primary Type'] == 'HOMICIDE')].groupby(['Year'])[['ID']].count().reset_index()
assaultArrest = df[(df.Arrest == 1) & (df['Primary Type'] == 'ASSAULT')].groupby(['Year'])[['ID']].count().reset_index()
assaultNotArrest = df[(df.Arrest == 0) & (df['Primary Type'] == 'ASSAULT')].groupby(['Year'])[['ID']].count().reset_index()
robberyArrest = df[(df.Arrest == 1) & (df['Primary Type'] == 'ROBBERY')].groupby(['Year'])[['ID']].count().reset_index()
robberyNotArrest = df[(df.Arrest == 0) & (df['Primary Type'] == 'ROBBERY')].groupby(['Year'])[['ID']].count().reset_index()

theft = df[(df['Primary Type'] == 'THEFT')].groupby(['Block'])[['ID']].count().reset_index()
theft = theft.sort_values(by=['ID'], ascending=False).head(10)
homicide = df[(df['Primary Type'] == 'HOMICIDE')].groupby(['Block'])[['ID']].count().reset_index()
homicide = homicide.sort_values(by=['ID'], ascending=False).head(10)
assault = df[(df['Primary Type'] == 'ASSAULT')].groupby(['Block'])[['ID']].count().reset_index()
assault = assault.sort_values(by=['ID'], ascending=False).head(10)
robbery = df[(df['Primary Type'] == 'ROBBERY')].groupby(['Block'])[['ID']].count().reset_index()
robbery = robbery.sort_values(by=['ID'], ascending=False).head(10)


df2012Arrest = df[(df.Year == 2012) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2012NotArrest = df[(df.Year == 2012) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2012Arrest = go.Bar(
    x = df2012Arrest['Primary Type'],
    y = df2012Arrest['ID'],
    name = 'Arrest'
)
bar2012NotArrest = go.Bar(
    x = df2012NotArrest['Primary Type'],
    y = df2012NotArrest['ID'],
    name = 'Not Arrest'
)
df2013Arrest = df[(df.Year == 2013) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2013NotArrest = df[(df.Year == 2013) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2013Arrest = go.Bar(
    x = df2013Arrest['Primary Type'],
    y = df2013Arrest['ID'],
    name = 'Arrest'
)
bar2013NotArrest = go.Bar(
    x = df2013NotArrest['Primary Type'],
    y = df2013NotArrest['ID'],
    name = 'Not Arrest'
)
df2014Arrest = df[(df.Year == 2014) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2014NotArrest = df[(df.Year == 2014) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2014Arrest = go.Bar(
    x = df2014Arrest['Primary Type'],
    y = df2014Arrest['ID'],
    name = 'Arrest'
)
bar2014NotArrest = go.Bar(
    x = df2014NotArrest['Primary Type'],
    y = df2014NotArrest['ID'],
    name = 'Not Arrest'
)
df2015Arrest = df[(df.Year == 2015) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2015NotArrest = df[(df.Year == 2015) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2015Arrest = go.Bar(
    x = df2015Arrest['Primary Type'],
    y = df2015Arrest['ID'],
    name = 'Arrest'
)
bar2015NotArrest = go.Bar(
    x = df2015NotArrest['Primary Type'],
    y = df2015NotArrest['ID'],
    name = 'Not Arrest'
)
df2016Arrest = df[(df.Year == 2016) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2016NotArrest = df[(df.Year == 2016) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2016Arrest = go.Bar(
    x = df2016Arrest['Primary Type'],
    y = df2016Arrest['ID'],
    name = 'Arrest'
)
bar2016NotArrest = go.Bar(
    x = df2016NotArrest['Primary Type'],
    y = df2016NotArrest['ID'],
    name = 'Not Arrest'
)
df2017Arrest = df[(df.Year == 2017) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2017NotArrest = df[(df.Year == 2017) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2017Arrest = go.Bar(
    x = df2017Arrest['Primary Type'],
    y = df2017Arrest['ID'],
    name = 'Arrest'
)
bar2017NotArrest = go.Bar(
    x = df2017NotArrest['Primary Type'],
    y = df2017NotArrest['ID'],
    name = 'Not Arrest'
)
df2018Arrest = df[(df.Year == 2018) & (df.Arrest == 1)].groupby(['Primary Type'])[['ID']].count().reset_index()
df2018NotArrest = df[(df.Year == 2018) & (df.Arrest == 0)].groupby(['Primary Type'])[['ID']].count().reset_index()
bar2018Arrest = go.Bar(
    x = df2018Arrest['Primary Type'],
    y = df2018Arrest['ID'],
    name = 'Arrest'
)
bar2018NotArrest = go.Bar(
    x = df2018NotArrest['Primary Type'],
    y = df2018NotArrest['ID'],
    name = 'Not Arrest'
)


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#ffffff',
    'text': '#000000'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Chicago Crime Visualization',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(id='graph1',
        figure={
            'data': [
                {'x': [2012,2013,2014,2015,2016,2017,2018], 'y': [year2012,year2013,year2014,year2015,year2016,year2017,year2018], 'type': 'line', 'name': 'Total Crime'}
            ],
            'layout': {
                'title': 'Total Crime By Year',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                    }

            }
        }
    ),

    dcc.Graph(id='graph2',
        figure={
            'data': [
                {'x': arrest['Year'], 'y': arrest['ID'], 'type': 'bar', 'name': 'Arrested'},
                {'x': notarrest['Year'], 'y': notarrest['ID'], 'type': 'bar', 'name': 'Not Arrested'},
            ],
            'layout': {
                'title': 'Total Arrested and Not Arrested Crime By Year',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                    }
            }
        }
    ),

     html.H3(
        children='Select Crime Type',
        style={
            'margin':30,
            'color': colors['text']
        }
    ),

    html.Div(
        [
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Theft', 'value': '1'},
                    {'label': 'Homicide', 'value': '2'},
                    {'label': 'Assault', 'value': '3'},
                    {'label': 'Robbery', 'value': '4'}
        ],
        value='1'
    )
    ],
    style={'margin':30, 'textAlign': 'center'},),

    html.Div(id='dropdown-output-container'),

     html.H3(
        children='Select Year To See Percentage of Each Crime Type',
        style={
            'margin':30,
            'color': colors['text']
        }
    ),

    html.Div(
        [
            dcc.Slider(
                id='my-slider',
                min=2012,
                max=2018,
                step=1,
                value=2012,
                marks={2012:'2012',2013:'2013',2014:'2014',2015:'2015',2016:'2016',2017:'2017',2018:'2018'}
            )
        ],
        style={'margin':30, 'textAlign': 'center'}),

    html.Div(id='slider-output-container'),

    html.H3(
        children='Select Crime Type To See Where It Occured Most(Top 10)',
        style={
            'margin':30,
            'color': colors['text']
        }
    ),

    html.Div(
        [
            dcc.Dropdown(
                id='my-dropdown2',
                options=[
                    {'label': 'Theft', 'value': '1'},
                    {'label': 'Homicide', 'value': '2'},
                    {'label': 'Assault', 'value': '3'},
                    {'label': 'Robbery', 'value': '4'}
        ],
        value='1'
    )
    ],
    style={'margin':30, 'textAlign': 'center'},),

    html.Div(id='dropdown-output-container2'),
    
    html.H3(
        children='Select Year',
        style={
            'margin':30,
            'color': colors['text']
        }
    ),
    html.Div(
        [
            dcc.Slider(
                id='my-slider2',
                min=2012,
                max=2018,
                step=1,
                value=2012,
                marks={2012:'2012',2013:'2013',2014:'2014',2015:'2015',2016:'2016',2017:'2017',2018:'2018'}
            )
        ],
        style={'margin':30, 'textAlign': 'center'}),

    html.Div(id='slider-output-container2')

])


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    if value == 2012:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2012['Primary Type'], 'values': df2012['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2012',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == 2013:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2013['Primary Type'], 'values': df2013['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2013',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == 2014:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2014['Primary Type'], 'values': df2014['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2014',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == 2015:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2015['Primary Type'], 'values': df2015['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2015',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == 2016:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2016['Primary Type'], 'values': df2016['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2016',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == 2017:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2017['Primary Type'], 'values': df2017['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2017',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == 2018:
        return html.Div([
            dcc.Graph(id='graph3',
                figure={
                'data': [
                    {'labels': df2018['Primary Type'], 'values': df2018['ID'], 'type': 'pie'}
                ],
                'layout': {
                    #'title': 'Crime Type in 2018',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])

@app.callback(
    dash.dependencies.Output('dropdown-output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output1(value):
    if value == '1':
        return html.Div([
            dcc.Graph(id='graph4',
                figure={
                'data': [
                    {'x': theftArrest['Year'], 'y': theftArrest['ID'], 'type': 'bar', 'name': 'Arrest'},
                    {'x': theftNotArrest['Year'], 'y': theftNotArrest['ID'], 'type': 'bar', 'name': 'Not Arrest'}
                ],
                'layout': {
                    'title': 'Theft: Arrest Vs Not Arrest By Year',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == '2':
        return html.Div([
            dcc.Graph(id='graph4',
                figure={
                'data': [
                    {'x': homicideArrest['Year'], 'y': homicideArrest['ID'], 'type': 'bar', 'name': 'Arrest'},
                    {'x': homicideNotArrest['Year'], 'y': homicideNotArrest['ID'], 'type': 'bar', 'name': 'Not Arrest'}
                ],
                'layout': {
                    'title': 'Homicide: Arrest Vs Not Arrest By Year',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == '3':
        return html.Div([
            dcc.Graph(id='graph4',
                figure={
                'data': [
                    {'x': assaultArrest['Year'], 'y': assaultArrest['ID'], 'type': 'bar', 'name': 'Arrest'},
                    {'x': assaultNotArrest['Year'], 'y': assaultNotArrest['ID'], 'type': 'bar', 'name': 'Not Arrest'}
                ],
                'layout': {
                    'title': 'Assault: Arrest Vs Not Arrest By Year',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])
    elif value == '4':
        return html.Div([
            dcc.Graph(id='graph4',
                figure={
                'data': [
                    {'x': robberyArrest['Year'], 'y': robberyArrest['ID'], 'type': 'bar', 'name': 'Arrest'},
                    {'x': robberyNotArrest['Year'], 'y': robberyNotArrest['ID'], 'type': 'bar', 'name': 'Not Arrest'}
                ],
                'layout': {
                    'title': 'Robbery: Arrest Vs Not Arrest By Year',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                        }
                }
            }
            )
        ])



@app.callback(
    dash.dependencies.Output('dropdown-output-container2', 'children'),
    [dash.dependencies.Input('my-dropdown2', 'value')])
def update_output3(value):
    if value == '1':
        return html.Div([
                dcc.Graph(id='graph5',
                figure={
                    'data': [
                        {'x': theft['Block'], 'y': theft['ID'], 'type': 'bar'}
                    ],
                    'layout': {
                        'title': '10 blocks where Theft occured most',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                            }
                    }
                }
            )
            ])
    elif value == '2':
        return html.Div([
                dcc.Graph(id='graph5',
                figure={
                    'data': [
                        {'x': homicide['Block'], 'y': homicide['ID'], 'type': 'bar'}
                    ],
                    'layout': {
                        'title': '10 blocks where Homicide occured most',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                            }
                    }
                }
            )
            ])
    elif value == '3':
        return html.Div([
                dcc.Graph(id='graph5',
                figure={
                    'data': [
                        {'x': assault['Block'], 'y': assault['ID'], 'type': 'bar'}
                    ],
                    'layout': {
                        'title': '10 blocks where Assault occured most',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                            }
                    }
                }
            )
            ])
    elif value == '4':
        return html.Div([
                dcc.Graph(id='graph5',
                figure={
                    'data': [
                        {'x': robbery['Block'], 'y': robbery['ID'], 'type': 'bar'}
                    ],
                    'layout': {
                        'title': '10 blocks where Robbery occured most',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                            }
                    }
                }
            )
            ])


@app.callback(
    dash.dependencies.Output('slider-output-container2', 'children'),
    [dash.dependencies.Input('my-slider2', 'value')])
def update_output4(value):
    if value == 2012:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2012Arrest, bar2012NotArrest],
                               layout=go.Layout(title='2012: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    elif value == 2013:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2013Arrest, bar2013NotArrest],
                               layout=go.Layout(title='2013: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    elif value == 2014:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2014Arrest, bar2014NotArrest],
                               layout=go.Layout(title='2014: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    elif value == 2015:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2015Arrest, bar2015NotArrest],
                               layout=go.Layout(title='2015: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    elif value == 2016:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2016Arrest, bar2016NotArrest],
                               layout=go.Layout(title='2016: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    elif value == 2017:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2017Arrest, bar2017NotArrest],
                               layout=go.Layout(title='2017: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    elif value == 2018:
        return html.Div([
                dcc.Graph(id='graph6',
                figure=go.Figure(data=[bar2018Arrest, bar2018NotArrest],
                               layout=go.Layout(title='2018: Arrest Vs Not Arrest For Each Crime Type', barmode='stack'))
              )
            ])
    

if __name__ == '__main__':
    app.run_server(debug=True)
