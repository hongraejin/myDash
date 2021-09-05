import dash_core_components as dcc

dcc.Graph(
    id='example',
    figure={
        'data':[
            {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'},
            {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':u'Montreal'}
        ],
        'layout':{
            'title':'Dash Data Visualization'
        }
    }
)

f