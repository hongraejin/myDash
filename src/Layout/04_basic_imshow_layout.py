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
app.layout = html.Div(
    [html.H3("Drag and draw annotations"), dcc.Graph(figure=fig, config=config),
     html.Div([
         dcc.Graph(figure=fig),
         dcc.Graph(figure=fig)
     ], style={'columnCount':2})

     ]
)

if __name__ == '__main__':
    app.run_server(debug=True)