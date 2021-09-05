import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import cv2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# barmode 는 Fruit Group 별로 나누어짐. color 는 City 열이므로 City에 의해 구분됨.
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

# fig2
img = cv2.imread("image.png")
fig2 = px.imshow(img)


app.layout = html.Div(
    children=[
        html.H1(children='Hello Bar Chart'),
        html.Div(children="Basic Application"),
        html.Div([
            dcc.Graph(
                id='example',
                figure=fig2
            ),
            dcc.Graph(
                id='example2',
                figure=fig2
            )],  className='row',style={'columnCount':2}),

        html.Div([
            dcc.Graph(
                id='example3',
                figure=fig2
            ),
            dcc.Graph(
                id='example4',
                figure=fig2
            ),
            dcc.Graph(
                id='example5',
                figure=fig2
            ),

        ], className='row', style={'columnCount': 3})

    ], # Graph 갯수에 맞추어서 style 이 구성됨
)

if __name__ == '__main__':
    app.run_server(debug=True)