import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

from app import app

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions


            """,className='mb-5',
        ),
        dcc.Markdown('#### Square footage'),
        dcc.Slider(
        id = 'sqft_living',
        min =300,
        max =7000,
        step=250,
        value=1500,
        marks={n: str(n) for n in range(500, 7000, 1000)},
        className='mb-5',
        ),
        dcc.Markdown('#### Bedrooms'),
        dcc.Dropdown(
        id='bedrooms',
        options = [
            {'label':'0', 'value':0},
            {'label':'1', 'value':1},
            {'label':'2', 'value':2},
            {'label':'3', 'value':3},
            {'label':'4', 'value':4},
            {'label':'5', 'value':5},
            {'label':'6', 'value':6},
            {'label':'7', 'value':7},
            {'label':'8', 'value':8},
            {'label':'9', 'value':9},
            {'label':'10', 'value':10},
        ],
        value = 1,
        className='mb-5',
        ),
        dcc.Markdown('#### Bathrooms'),
        dcc.Dropdown(
        id='bathrooms',
        options = [
            {'label':'1', 'value':1},
            {'label':'1.5', 'value':1.5},
            {'label':'2', 'value':2},
            {'label':'2.5', 'value':2.5},
            {'label':'3', 'value':3},
            {'label':'3.5', 'value':3.5},
            {'label':'4', 'value':4},
            {'label':'4.5', 'value':4.5},
            {'label':'5', 'value':5},
            {'label':'5.5', 'value':5.5},
            {'label':'6', 'value':6},

        ],
        value = 1,
        className='mb-5',
        ),

        dcc.Markdown('Note* This interactive predictor is a simplified version of my model. The full version uses more features as demonstrated on the Explain page '),

    ],
    md=4,
)

column2 = dbc.Col(
    [


        dcc.Markdown('#### Year built'),
        dcc.Slider(
        id = 'yr_built',
        min =1900,
        max =2014,
        step=10,
        value=1950,
        marks={n: str(n) for n in range(1900, 2014, 25)},
        className='mb-5'
        ),

        dcc.Markdown('#### Floors'),
        dcc.Dropdown(
        id='floors',
        options = [
            {'label':'1', 'value':1},
            {'label':'2', 'value':2},
        ],
        value=1,
        className='mb-5',
        ),
        dcc.Markdown('#### Waterfront'),
        dcc.Dropdown(
        id = 'waterfront',
        options=[
            {'label': 'Yes', 'value' : 1},
            {'label': 'No', 'value' : 0},
        ],
        value=0,
        className='mb-5',
        ),

    ],
    md=4,
)
column3 = dbc.Col(
    [
        html.H2('Price of home', className='mb-5'),
        html.Div(id='prediction-content', className='lead'),

    ],
)
import pandas as pd
import numpy as np
@app.callback(
    Output('prediction-content', 'children'),
    [
    Input('bedrooms', 'value'),
    Input('bathrooms', 'value'),
    Input('sqft_living','value'),
    Input('floors','value'),
    Input('waterfront','value'),
    Input('yr_built','value'),
    ],
)
def predict(beds,baths,sqft,floor, water, yr):
    df = pd.DataFrame(
        columns=['bedrooms', 'bathrooms','sqft_living','floors', 'waterfront', 'condition', 'grade', 'yr_built'],
        data=[[ beds, baths, sqft, floor, water, 3, 7, yr]]
    )
    y_pred_log=pipeline.predict(df)[0]
    y_pred = round(np.expm1(y_pred_log),0)

    return f'${y_pred:.0f}'

layout = dbc.Row([column1, column2, column3])
