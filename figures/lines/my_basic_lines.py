import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
print('Random seed initialised')
xx = np.linspace(0,1,100)
yy = np.random.randn(100)

trace0 = go.Scatter(x=xx,y=yy+5.,
                   mode='markers',name='markers')
trace1 = go.Scatter(x=xx,y=yy,
                   mode='lines',name='lines')
trace2 = go.Scatter(x=xx,y=yy-5.,
                   mode='lines+markers',name='lines+markers')
#names are for the hovering and legend
data =  [trace0,trace1,trace2]

# Title, axis, what happens when hovering
layout = go.Layout(title='Line chart') # it's optional

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='lines.html',auto_open=False)
