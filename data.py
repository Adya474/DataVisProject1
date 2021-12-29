import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

mean = df.groupby(["student_id","level"], as_index=False)["attempt"].mean()

fig=go.Figure(go.Scatter(
    x=df.groupby("level")["attempt"].mean(),
    y=["Level 1", "Level 2", "Level 3", "Level 4"],  
))

fig1 = px.scatter(mean, x="student_id", y="level", size="attempt",color="attempt")

fig.show()
fig1.show()