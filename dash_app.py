# Task 3
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

app.layout = html.Div([
    html.H1('Pink Morsel Sales Analysis'),
    dcc.Graph(id='pink',
              figure=fig),
    dcc.Dropdown(id='region-picker',
                 options=[{'label': region, 'value': region} for region in df['region'].unique()],
                 value=['north', 'south', 'east', 'west'],
                 multi=True)
])
@app.callback(
    Output('pink', 'figure'),
    [Input('region-picker', 'value')])

def update_figure(selected_region):
    filtered_df = df[df['region'].isin(selected_region)]
    fig = px.line(filtered_df, x='date', y='sales', color='region')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)