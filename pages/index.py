import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has
twelve columns.

There are three main layout components in dash-bootstrap-components: Container,
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column
should take up a third of the width. Since we don't specify behaviour on
smallersize screens Bootstrap will allow the rows to wrap so as not to squash
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predict the price of a 🏠 in King County WA

            Are you in the market for a new home?

            Are you trying to determine what size house will fall within your budget?

            Will you be able to afford the house of your dreams? The one that overlooks the water?


            With this price predictor you can quickly and easily enter a few simple options and recieve an estimated home price instantly!








            """
        ),
        dcc.Link(dbc.Button('Get home prices', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(html.Img(src='assets/prices.jpg', className='img-fluid'))

layout = dbc.Row([column1, column2])
