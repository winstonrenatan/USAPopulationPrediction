import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd

from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server
app.title = 'RO Projects'
df = pd.read_csv(r'USAPopDeciEdit.csv',engine='python',encoding='latin1')

# choose only certain column
df = df[["state_id","state_name","county_name","lat","lng","FUNCSTAT","2010","2011","2012","2013","2014","2015","2016","2017PREDINT","2018PREDINT","2019PREDINT","2020PREDINT"]].drop_duplicates()

app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

for col in df.columns:
    df[col] = df[col].astype(str)

# Display the info in the box
df['text'] = df['county_name'] + ', ' + df['state_id'] + '<br>' + \
    df['FUNCSTAT'] + '<br>'+\
    '2010 :' + df['2010'] + '<br>' + \
    '2011 :' + df['2011'] + '<br>' + \
    '2012 :' + df['2012'] + '<br>' + \
    '2013 :' + df['2013'] + '<br>' + \
    '2014 :' + df['2014'] + '<br>' + \
    '2015 :' + df['2015'] + '<br>'+ \
    '2016 :' + df['2016'] + '<br>'+ \
    '2017 :' + df['2017PREDINT'] + '<br>'+ \
    '2018 :' + df['2018PREDINT'] + '<br>'+ \
    '2019 :' + df['2019PREDINT'] + '<br>'+ \
    '2020 :' + df['2020PREDINT']

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]


layout_table = dict(
    autosize=True,
    height=500,
    font=dict(color="rgb(255,255,255)"),
    titlefont=dict(color="rgb(255,255,255)", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    )
layout_table['font-size'] = '12'
layout_table['margin-top'] = '20'


layout_map = dict(
        title = 'USA POPULATION'+ '<br>' + \
                'This software will display the population spreaded in the map of United States of America,which have real data from 2010-2016 while prediction from 2017-2020.'+ '<br>' + \
                'Here there are some filter that are available using the states and also FUNCSTAT.',
        colorbar = True,
        autosize = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(0, 0,0)",
            countrycolor = "rgb(162, 162, 162)",
            countrywidth = 2,
            subunitwidth = 2
        ),
        height = 800,
        width = 1500
    )

def gen_map(df):
    return{
        "data":[{
            "type" : "scattergeo",
            "locationmode" : "USA-states",
            "lon" : list(df['lng']),
            "lat" : list(df['lat']),
            "text" :list(df['text']),
            "mode" : "marker",
            "markers" : [{
                    "size" : 5,
                    "opacity" :0.8,
                    "reversescale" : True,
                    "autocolorscale" : False,
                    "symbol" : "circle",
                    "line" : [{
                        "width" : 1,
                        "color": "rgb(162, 162, 162 )"
                    }],
                    "colorscale" : "scl",
                    }]
            }],
        "layout": layout_map
    }

fig = dict( layout=layout_map )    

app.layout  = html.Div(
    html.Div([
    html.Div(
                [
                    # Header
                    html.H1 (children="US Public Assistant for woman and children",
                             className="nine columns"),
                    html.Div(children=''' 
                            Dash app for RO Projects
                            ''',
                             className="nine columns"
                    )
                ], className="row"
            ),
    #selectors
    html.Div([

        html.Div(
             [
                html.P('Choose State:'),
                dcc.Checklist(
                    id = 'State',
                    options=[
                            {'label': 'Alabama', 'value': 'AL'},
                            {'label': 'Alaska', 'value': 'AK'},
                            {'label': 'Arizona' , 'value': 'AZ'},
                            {'label': 'Arkansas', 'value': 'AR'},
                            {'label': 'California ', 'value': 'CA'},
                            {'label': 'Colorado', 'value': 'CO'},
                            {'label': 'Connecticut', 'value': 'CT'},
                            {'label': 'Delaware', 'value': 'DE'},
                            {'label': 'Florida', 'value': 'FL'},
                            {'label': 'Georgia', 'value': 'GA'},
                            {'label': 'Hawaii', 'value': 'HI'},
                            {'label': 'Idaho', 'value': 'ID'},
                            {'label': 'Illinois', 'value': 'IL'},
                            {'label': 'Indiana', 'value': 'IN'},
                            {'label': 'Iowa', 'value': 'IA'},
                            {'label': 'Kansas', 'value': 'KS'},
                            {'label': 'Kentucky', 'value': 'KY'},
                            {'label': 'Louisiana', 'value': 'LA'},
                            {'label': 'Maine', 'value': 'ME'},
                            {'label': 'Maryland', 'value': 'MD'},
                            {'label': 'Massachusetts', 'value': 'MA'},
                            {'label': 'Michigan', 'value': 'MI'},
                            {'label': 'Minnesota', 'value': 'MN'},
                            {'label': 'Mississipi', 'value': 'MS'},
                            {'label': 'Missouri', 'value': 'MO'},
                            {'label': 'Montana', 'value': 'MT'},
                            {'label': 'Nebraska', 'value': 'NE'},
                            {'label': 'Nevada', 'value': 'NV'},
                            {'label': 'New Hampshire', 'value': 'NH'},
                            {'label': 'New Jersey', 'value': 'NJ'},
                            {'label': 'New Mexico', 'value': 'NM'},
                            {'label': 'New York', 'value': 'NY'},
                            {'label': 'North Carolina', 'value': 'NC'},
                            {'label': 'North Dakota', 'value': 'ND'},
                            {'label': 'Ohio', 'value': 'OH'},
                            {'label': 'Oklahoma', 'value': 'OK'},
                            {'label': 'Oregon', 'value': 'OR'},
                            {'label': 'Pennyslvania', 'value': 'PA'},
                            {'label': 'Rhode Island', 'value': 'RI'},
                            {'label': 'South Carolina', 'value': 'SC'},
                            {'label': 'South Dakota', 'value': 'SD'},
                            {'label': 'Tennessee', 'value': 'TN'},
                            {'label': 'Texas', 'value': 'TX'},
                            {'label': 'Utah', 'value': 'UT'},
                            {'label': 'Vermont', 'value': 'VT'},
                            {'label': 'Virginia', 'value': 'VA'},
                            {'label': 'Washington', 'value': 'WA'},
                            {'label': 'West Virginia', 'value': 'WV'},
                            {'label': 'Wisconsin', 'value': 'WI'},
                            {'label': 'Wyoming', 'value': 'WY'},
                    ],
                    values =['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'],
                    labelStyle={'display': 'inline-block'}
                ),
        ]
        ),
         html.Div(
                    [
                        html.P('FuncStat:'),
                        dcc.Dropdown(
                            id='funcstat',
                            options= [{'label': str(item),
                                                  'value': str(item)}
                                                 for item in set(df['FUNCSTAT'])],
                            multi=True,
                            value=list(set(df['FUNCSTAT']))
                        )
                    ],
                    style={'margin-top': '10'}
                )
            ],
            className='row'
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id='map-graph',
                                  animate=True,
                                  style={'margin-top': '20'})
                    ], className = "six columns"
                ),
                html.Div(
                    [
                        html.H1(children="The Data Table",
                                className="nine columns"),
                        dt.DataTable(
                            rows=df.to_dict('records'),
                            columns=df.columns,
                            row_selectable=True,
                            filterable=True,
                            sortable=True,
                            selected_row_indices=[],
                            id='datatable'),
                    ],
                    style = layout_table,
                    className="six columns"
                ),
            ], className="row"
        )
],className='ten columns offset-by-one'
))

@app.callback(
    Output('map-graph', 'figure'),
    [Input('datatable', 'rows'),
     Input('datatable', 'selected_row_indices')])
def map_selection(rows, selected_row_indices):
    aux = pd.DataFrame(rows)
    temp_df = aux.iloc[selected_row_indices, :]
    if len(selected_row_indices) == 0:
        return gen_map(aux)
    return gen_map(temp_df)

@app.callback(
    Output('datatable', 'rows'),
    [Input('funcstat', 'value'),
     Input('State', 'values')])
def update_selected_row_indices(funcstat, State):
    map_aux = df.copy()

    # Type filter
    map_aux = map_aux[map_aux['FUNCSTAT'].isin(funcstat)]
    # Boroughs filter
    map_aux = map_aux[map_aux["state_id"].isin(State)]

    rows = map_aux.to_dict('records')
    return rows


if __name__ == '__main__':
    app.run_server(debug=True)