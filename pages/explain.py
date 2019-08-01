import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Explain

            These predictions were created using data from home sales taken in King County, WA in 2015.

            Originally an XGBoost Regressor model was trained on the entire 21 feature dataset.  Due to time constraints and not wanting to overload the end user with options, I trimmed down the dataset to the 7 features that a prospective homebuyer would be most interested in.

            I will be doing a side by side comparison of the original model on the full data set, and the trimmed data set.


            """
        ),
        html.Img(src='assets/feature_importances_full.jpg', className='img-fluid'),
    ],
    md=12,

)


column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1])
