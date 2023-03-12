import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

## Define the app
app = dash.Dash(__name__)

## Reading it in, keeping only volume
dat = pd.read_csv("https://raw.githubusercontent.com/bcaffo/ds4bme_intro/master/data/kirby21.csv")
dat = dat.drop(['Unnamed: 0'],\
             axis = 1)


dat = dat.assign(id_char = "id_"+dat.id.astype(str))


## Produce the figure
fig = px.bar(dat, x = "id_char", y = "volume", color = "roi")
fig.show()
## This creates the layout of the page
app.layout = html.Div(children=[
    ## HTML elements added with html.method
    html.H1(children='Subject level compositional data'),
    
    ## Dynamic graph is added with dcc.METHOD (dcc = dynamic core component)
    dcc.Graph(
        id = 'graph',
        figure = fig
    )
])

## This runs the server
if __name__ == '__main__':
    app.run_server(debug=True)