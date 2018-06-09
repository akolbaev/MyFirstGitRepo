import os
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd
from numbers import Number
import plotly
import base64
import json
import io

def as_dollar(v):  
    """Convert number to percentage string."""
    if isinstance(v, Number):
        return "${:,.2f}".format(v)
    else:
        raise TypeError("Numeric type required")


df = pd.read_excel('a.xlsx', sheetname='Sheet1')

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H2('Hello World by kinetikos!!!???!'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)







app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
