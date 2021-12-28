import pandas as pd
import plotly.express as px
df=pd.read_csv("C:/Users/lenovo/Desktop/Python/Class 103/csv files/ProjectData.csv")
fig=px.scatter(df, x="date", y="cases", color="country", title="Covid-19 Cases-2020")
fig.show()
print("Choose your Browser as a file to open with and click on the checkbox for easy access for the other times.")
print("Now open your Browser.")