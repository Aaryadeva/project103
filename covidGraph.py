import pandas as pd
import plotly_express as px

file=pd.read_csv('Data.csv')
fig=px.scatter(file,x='date',y='cases',color='country')
fig.show()