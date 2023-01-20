from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, dashboards, extratos

# DataFremes and Dcc.store

df_receitas = pd.read_csv('df_receitas.csv', index_col=0, parse_dates=True)
df_receita_aux = df_receitas.to_dict()






# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[





], fluid=True,)




if __name__ == '__main__':
    app.run_server(port=8051, debug=True)