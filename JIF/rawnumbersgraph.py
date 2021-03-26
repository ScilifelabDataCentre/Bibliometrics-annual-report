import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
#below for fellows - use 'Year' as x axis and grouping variable
#JIFscore = pd.read_excel('/Users/liahu895/Documents/scilifelab/Python/rawdbnumbers/fellows_matchingcomplete.xlsx', sheet_name = 'Sheet1', header =0, engine='openpyxl',keep_default_na=False)
#below for facilities -  use 'Year' as x axis and grouping variable
#JIFscore = pd.read_excel('/Users/liahu895/Documents/scilifelab/Python/rawdbnumbers/rawnumbersfinalmatchedfac.xlsx', sheet_name = 'Sheet1', header =0, engine='openpyxl',keep_default_na=False)
#below for affiliates - use 'Publication_year_y' as x axis and grouping variable
JIFscore = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /FinalKTHdata/Stitcheddata/affiliates_JIF_statsinc.xlsx', sheet_name = 'Sheet1', header =0, engine='openpyxl',keep_default_na=False)
JIFscore['Impact Factor without Journal Self Cites'] = pd.to_numeric(JIFscore['Impact Factor without Journal Self Cites'])
JIFscoresub = JIFscore[['Publication_year_y', 'Impact Factor without Journal Self Cites']]
#set all blank values to -1 - for when JIF is unknown (e.g. journal nott in JIF score list)
modJIFscoresub = JIFscoresub.fillna(-1)
modJIFscoresub['JIFcat'] = pd.cut(modJIFscoresub['Impact Factor without Journal Self Cites'], bins = [-1, -0.000000001, 6, 9, 25, 1000], include_lowest=True, labels=['JIF unknown','JIF <6', 'JIF 6-9', 'JIF 9-25', 'JIF >25']) 
catJIFsub = modJIFscoresub[['Publication_year_y', 'JIFcat']]
catJIFsub['Publication_year_y'] = pd.to_numeric(catJIFsub['Publication_year_y'])
#filter to include the correct years 
JIFyear = catJIFsub[(catJIFsub['Publication_year_y'] > 2014) & (catJIFsub['Publication_year_y'] < 2021)]
JIFcounts = JIFyear.value_counts(['Publication_year_y', 'JIFcat']).reset_index()
JIFcounts.columns = ['Publication_year_y', 'JIFcat', 'Count']
# Require the data as an Excel file that can be shared with Alice 
JIFcounts.sort_values(['Publication_year_y', 'JIFcat'], ascending=[True, True], inplace=True)
#below to generate fellows table 
#JIFcounts.to_excel('/Users/liahu895/Documents/scilifelab/Python/rawdbnumbers/fellows_JIFscoresmatched.xlsx')
# Need to seperate out the data to prepare for a stacked barchart  
UnknownJIF = JIFcounts[(JIFcounts['JIFcat'] == 'JIF unknown')]
Undersix = JIFcounts[(JIFcounts['JIFcat'] == 'JIF <6')]
sixtonine = JIFcounts[(JIFcounts['JIFcat'] == 'JIF 6-9')]
ninetotwentyfive = JIFcounts[(JIFcounts['JIFcat'] == 'JIF 9-25')]
overtwentyfive = JIFcounts[(JIFcounts['JIFcat'] == 'JIF >25')]
# Make stacked bar chart 
fig = go.Figure(data=[
    go.Bar(name='JIF okänt', x = UnknownJIF.Publication_year_y, y = UnknownJIF.Count, marker_color = ('rgb(167,201,71)')),
    go.Bar(name='JIF < 6', x = Undersix.Publication_year_y, y = Undersix.Count, marker_color = ('rgb(167,201,71)')),
    go.Bar(name='JIF 6 - 9', x = sixtonine.Publication_year_y, y = sixtonine.Count, marker_color = ('rgb(167,201,71)')),
    go.Bar(name='JIF 9 - 25', x = ninetotwentyfive.Publication_year_y, y = ninetotwentyfive.Count, marker_color = ('rgb(167,201,71)')),
    go.Bar(name='JIF > 25', x = overtwentyfive.Publication_year_y, y = overtwentyfive.Count, marker_color = ('rgb(167,201,71)'))    
])
fig.update_layout(barmode='stack', plot_bgcolor='white', font=dict(size=40), margin=dict(r=150), width = 1500, height = 1500, showlegend=False)
fig.update_traces(marker_line_width=0)
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
#fellows range
#    range=[0,161])
#affiliates range
    range=[0,901])
#facilities range
#    range=[0,801])
fig.show()