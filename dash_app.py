# Task 3 and Task 4
# Run this app with 'python dash_app.py` and
# visit http://127.0.0.1:8050/ in web browser
# Type "control + c" to exit server

import pandas as pd
from dash import dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('data/total_sales_ps_dropped.csv')
fig = px.line(df, x='date', y='sales')

app = dash.Dash(__name__)

options = {
    'north': ['north'],
    'south': ['south'],
    'east': ['east'],
    'west': ['west'],
    'all': ['north', 'south', 'east', 'west']
}

app.layout = html.Div([
    html.H1(children='Pink Morsel Sales Analysis', style={'textAlign': 'center', 'color': 'hotpink'}),
    dcc.Graph(id='pink',
              figure=fig),
    dcc.RadioItems(id='region-picker',
                   options=[{'label': region, 'value': region} for region in options.keys()],
                   value='all',
                   inline=True,
                   style={'textAlign': 'center', 'font-size': 20, 'font-weight': 'bold'},
                   ),
])
@app.callback(
    Output('pink', 'figure'),
    [Input('region-picker', 'value')])

def update_figure(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].isin([selected_region])]
    fig = px.line(filtered_df, x='date', y='sales', color='region')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)