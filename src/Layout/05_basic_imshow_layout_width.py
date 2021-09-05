import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import cv2

img = cv2.imread('image.png')

fig = px.imshow(img)
fig.update_layout(dragmode='drawrect')
config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ]
}

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div(
        [dcc.Graph(id='example', figure=fig)],
        style={'width':"50%", 'padding':"0 0"}
    ),
    html.Div(
        [dcc.Graph(id='example2', figure=fig)],
      style={'width':'40%'}
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)