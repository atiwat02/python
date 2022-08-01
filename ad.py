from dash import Dash, dcc, html, Input, Output, State
from sklearn.svm import SVC
import numpy as np


clf = SVC()
clf.fit(np.array([[83, 86, 0], [64, 65, 1], [72, 90, 1], [81, 75, 0], [70, 96, 0], [68, 80, 0], [65, 70, 1], [75, 80, 0], [71, 91, 1], [85, 85, 0],
        [80, 90, 1], [72, 95, 0], [69, 70, 0], [75, 70, 1]]), np.array(['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no']))


app = Dash(__name__)

app.layout = html.Div([
    html.Label("Temperature : "),
    dcc.Input(id='input-on-submit1', type='text'),
    html.Br(),
    html.Label("Humidity : "),
    dcc.Input(id='input-on-submit2', type='text'),
    html.Br(),
    html.Label("Windy : "),
    dcc.Dropdown(options=[
        {'label': 'FALSE', 'value': 1},
        {'label': 'TRUE', 'value': 0},
    ], id='input-on-submit3'),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit1', 'value'),
    State('input-on-submit2', 'value'),
    Input('input-on-submit3', 'value')
)
def update_output(n_clicks, value1, value2, value3):

    test1 = [value1, value2, value3]

    return 'ผลการทำนาย คือ ::  {} '.format(
        list(clf.predict([test1]))
    )


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port='7080')
