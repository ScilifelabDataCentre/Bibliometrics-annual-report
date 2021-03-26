import pandas as pd
import plotly.express as px
JIFscore = pd.read_excel('/Users/liahu895/Documents/scilifelab/Python/JIF/JIFabove9.xlsx', sheet_name = 'Sheet 1', header =0, engine='openpyxl',keep_default_na=False)
fig = px.bar(data_frame = JIFscore, x="Year", y="Affiliates", width = 1500, height = 1500)
#change bar colours to match visual identity 2020
fig.update_traces(marker_color = 'rgb(167,201,71)')
# change background colour and general font
fig.update_layout(plot_bgcolor='white', font=dict(size=40), margin=dict(r=150))
#modify x-axis
fig.update_xaxes(title = " ", 
    showgrid=True, 
    linecolor='black', 
#Modify text and values to reflect appropriate range (can do all years, or just consistent with leiden. For 2020 = 2015-2020)
    ticktext=["<b>2015</b>", "<b>2016</b>", "<b>2017</b>", "<b>2018</b>", "<b>2019</b>", "<b>2020</b>"], 
    tickvals=["2015", "2016", "2017", "2018", "2019", "2020"])
#modify y-axis
fig.update_yaxes(title = " ", 
    showgrid=True, 
    gridcolor="black", 
    linecolor='black', 
#change range to envelope the appropriate range
    ticktext=["0,00", "0,05", "0,10", "0,15", "0,20", "0,25", "0,30"], 
    tickvals=["0.0", "0.05", "0.1", "0.15", "0.20", "0.25", "0.30"],
    range=[0,0.31])
fig.show()


