# Task 5
# Run pytest to run tests

import dash
from dash import html, dcc
import time


#Test 1 -The header is present
def test_header_present(dash_duo):
    dash_app = dash.Dash(__name__)
    dash_app.layout = html.Div([html.H1(children='Pink Morsel Sales Analysis')])
    dash_duo.start_server(dash_app)
    time.sleep(2)
    assert dash_duo.wait_for_text_to_equal('H1', 'Pink Morsel Sales Analysis', timeout=10)

#Test 2 - The visualisation is present.
def test_visualisation_present(dash_duo):
    dash_app = dash.Dash(__name__)
    dash_app.layout = html.Div([dcc.Graph(id='pink')])
    dash_duo.start_server(dash_app)
    assert dash_duo.wait_for_element_by_id('pink', timeout=10)

#Test 3 - The region picker is present.
def test_region_picker_present(dash_duo):
    dash_app = dash.Dash(__name__)
    dash_app.layout = html.Div([dcc.RadioItems(id='region-picker')])
    dash_duo.start_server(dash_app)
    assert dash_duo.wait_for_element_by_id('region-picker', timeout=10)