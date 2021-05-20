# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:35:41 2021

@author: eiken
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
# import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd
# import datetime
# import plotly.graph_objects as go

# -------- Python Functions 
# def cast_list(test_list, data_type):
#     return list(map(data_type, test_list))

# -------- Load Data
# text_file = open(r"C:\Users\eiken\OneDrive\Documents\MATLAB\Research Misc\sout00000001", "r")
# lines = text_file.readlines()
# text_file.close()


# type(lines)
# type(lines[1])

# # -------- Create DataFrame and correct data types
# df = pd.DataFrame()

# for i in lines :
#     newlist = i.split()
#     newdata = pd.DataFrame(cast_list(newlist, float))
#     newdata = newdata.swapaxes(0, 'columns')
#     df = pd.concat([df, newdata])

# df.rename({0 :'Time'}, axis = 'columns')

# fig = plt.semilogy(df[0], df[6])
# fig
# type(fig)

# fig = plt.plot(df[0], df[6])
# plt.yscale('log')
# fig

# px.scatter(df[0], df[6])



# -------- Loads data from plain text to data frame
df = pd.read_csv(r"C:\Users\eiken\OneDrive\Documents\MATLAB\Research Misc\sout00000001",
                   sep="   ",
                   header=None,
                   engine='python')

# -------- Creates App

app = dash.Dash()

app.layout = html.Div([
    html.H1("TITLE HERE"),
    
    
    html.Label('Select a species to observe:'),
    html.Div([ 
        dcc.Dropdown( 
            id='species',
            options=[{'label': 'FXa', 'value': 6},
                     {'label': 'Thrombin', 'value' : 22}],
            value = 6
            )
        ], 
        style = {'width' : '48%'}),

    
    dcc.Graph(id='plot')     
 
    
    ])



@app.callback(
     Output('plot', component_property ='figure'),
     Input('species', component_property = 'value')
     )


def update_figure(species_choice):
    
    # fig = plt.semilogy(df[0], df[species_choice])
    fig = px.line(df, x = 0, y = species_choice, log_y = True)
    
    fig.update_yaxes(title = 'Thrombin (nM)')
    fig.update_xaxes(title = "Time")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    