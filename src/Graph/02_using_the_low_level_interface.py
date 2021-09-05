import dash_core_components as dcc
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(x=[1,2,3], y=[4,1,2])]
)
dcc.Graph(
    id='example',
    figure=fig
)
fig.show()