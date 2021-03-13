import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import uvicorn as uvicorn
from dash.dependencies import Input, Output
from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

app = dash.Dash(__name__, requests_pathname_prefix='/cos/')

f = 4.0
t = np.arange(0, 2, 0.001)
cos_wave = np.cos(2*np.pi*f*t)

df = pd.DataFrame({"Time":t, "Amplitude":cos_wave})



r_cord = []
min_freq_range = 0.0
max_freq_range = 10.0
sf_list = np.arange(min_freq_range, max_freq_range, 0.1)

for sf in sf_list:
    r_cord.append([(cos_wave[i], t[i]*sf*2*np.pi) for i in range(len(t))])



fig = px.scatter(df, x="Time", y="Amplitude")

fig2 = px.scatter_polar(r_cord[0], r_cord[1])

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='example-',
        figure=fig2
    )
])

if __name__ == "__main__":
    server = FastAPI()
    server.mount("/cos", WSGIMiddleware(app.server))
    uvicorn.run(server)