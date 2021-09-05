import dash_core_components as dcc
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x='sepal_width',y='sepal_length')
dcc.Graph(figure=fig)
fig.show()