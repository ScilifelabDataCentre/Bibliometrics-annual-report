import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
JIFscore = pd.read_excel('/Users/liahu895/Documents/scilifelab/Python/JIF/JIFscores.xlsx', sheet_name = 'DJR_5847', header =0, engine='openpyxl',keep_default_na=False)
extract = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /FinalKTHdata/Stitcheddata/fellows_compiled_JIFaligned.xlsx', sheet_name = 'Sheet1', header =0, engine='openpyxl',keep_default_na=False)
#Take just the columns of interest forward for the join
extractlow = extract.apply(lambda x: x.astype(str).str.lower())
scoresubs = JIFscore[['Full Journal Title', 'Impact Factor without Journal Self Cites']]
scoresubslow = scoresubs.apply(lambda x: x.astype(str).str.lower())
#can join on ISSN with a direct extract from publications databases, or on 'journal' from KTH data (check names for matching in the case of the latter)
#need to modify columns, only need on= and col names if col names shared. However, need left_on=[] and right_on=[] with 'df_col' if the column names differ  
mergeJIF = pd.merge(extractlow, scoresubslow, how='left', left_on=['journal_y'], right_on=['Full Journal Title'])
#To remove any potential duplicates 
mergeJIF.drop_duplicates(subset="UT", keep='first', inplace=True)
####Uncomment below to check the alignment of journals - see if manual improvement is possible 
####mergeJIF.to_excel('/Users/liahu895/Documents/scilifelab/Python/JIF/checkmatchingfell_v4.xlsx')
#categorise JIF
mergeJIF['Impact Factor without Journal Self Cites'] = pd.to_numeric(mergeJIF['Impact Factor without Journal Self Cites'])
mergeJIFsub = mergeJIF[['Publication_year_y', 'Doc_type_code_rev_y', 'Impact Factor without Journal Self Cites']]
#set all blank values to -1 - for when JIF is unknown (e.g. journal nott in JIF score list)
modmergeJIFsub = mergeJIFsub.fillna(-1)
modmergeJIFsub['JIFcat'] = pd.cut(modmergeJIFsub['Impact Factor without Journal Self Cites'], bins = [-1, 0, 6, 9, 25, 1000], include_lowest=True, labels=['JIF unknown','JIF <6', 'JIF 6-9', 'JIF 9-25', 'JIF >25']) 
#To write out in case of checking output
modmergeJIFsub.to_excel('/Users/liahu895/Documents/scilifelab/Python/JIF/CHECKFELLOWSV2.xlsx')
catJIFsub = modmergeJIFsub[['Publication_year_y', 'Doc_type_code_rev_y','JIFcat']]
#filter to include only the correct document types 
JIFrevarts= catJIFsub[(catJIFsub['Doc_type_code_rev_y'] == 'rv') | (catJIFsub['Doc_type_code_ref_y'] == 'ar')]
JIFrevarts['Publication_year_y'] = pd.to_numeric(JIFrevarts['Publication_year_y'])
#filter to include the correct years 
JIFrevartsyear = JIFrevarts[(JIFrevarts['Publication_year_y'] > 2014) & (JIFrevarts['Publication_year_y'] < 2021)]
JIFcounts = JIFrevartsyear.value_counts(['Publication_year_y', 'JIFcat']).reset_index()
JIFcounts.columns = ['Year', 'JIFcat', 'Count']
# Require the data as an Excel file that can be shared with Alice 
JIFcounts.sort_values(['Year', 'JIFcat'], ascending=[True, True], inplace=True)
JIFcounts.to_excel('/Users/liahu895/Documents/scilifelab/Python/JIF/Finalised data/Fellows_v2.xlsx')
# Need to seperate out the data to prepare for a stacked barchart  
UnknownJIF = JIFcounts[(JIFcounts['JIFcat'] == 'JIF unknown')]
Undersix = JIFcounts[(JIFcounts['JIFcat'] == 'JIF <6')]
sixtonine = JIFcounts[(JIFcounts['JIFcat'] == 'JIF 6-9')]
ninetotwentyfive = JIFcounts[(JIFcounts['JIFcat'] == 'JIF 9-25')]
overtwentyfive = JIFcounts[(JIFcounts['JIFcat'] == 'JIF >25')]
# Make stacked bar chart 
fig = go.Figure(data=[
    go.Bar(name='JIF okänt', x = UnknownJIF.Year, y = UnknownJIF.Count, marker_color = ('rgb(166,166,166)')),
    go.Bar(name='JIF < 6', x = Undersix.Year, y = Undersix.Count, marker_color = ('rgb(73,31,83)')),
    go.Bar(name='JIF 6 - 9', x = sixtonine.Year, y = sixtonine.Count, marker_color = ('rgb(4,92,100)')),
    go.Bar(name='JIF 9 - 25', x = ninetotwentyfive.Year, y = ninetotwentyfive.Count, marker_color = ('rgb(167,201,71)')),
    go.Bar(name='JIF > 25', x = overtwentyfive.Year, y = overtwentyfive.Count, marker_color = ('rgb(76, 151,159)'))    
])
fig.update_layout(barmode='stack', plot_bgcolor='white', font=dict(size=18), margin=dict(r=150), width = 600, height = 600, showlegend=True)
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
    range=[0,150])
fig.show()