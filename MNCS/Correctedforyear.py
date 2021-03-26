import pandas as pd
import numpy as np
import plotly.express as px
#read in the data 
pubs = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /FinalKTHdata/Stitcheddata/Facilities_reportingexclusive.xlsx', sheet_name='Sheet1', header=0, engine='openpyxl',keep_default_na=False)
#need to filter dataframes to include only the years to be included this time (2020 is 2015-2018). UNCOMMENT THIS
pubs_type = pubs[(pubs['Doc_type_code_rev_y'] == 'rv') | (pubs['Doc_type_code_rev_y'] == 'ar')]
filt_year = pubs_type[(pubs_type['Publication_year_y'] > 2014) & (pubs_type['Publication_year_y'] < 2019)]
# subset to work with less data - for MNCS only need year and cf_scxwo from here 
subset_filt = filt_year[['Publication_year_y', 'cf_scxwo_y']]
# need to drop 'nones' as these are unknown 
subset_filt['cf_scxwo_y'].replace('None', np.nan, inplace=True)
subset_filt.dropna(subset=['cf_scxwo_y'], inplace=True)
subset_filt['cf_scxwo_y']= pd.to_numeric(subset_filt['cf_scxwo_y'], downcast="float")
# to get MNCS you need to calculate the mean of the cf_scxwo column for each year
#MNCS_y = subset_filt.groupby(['Publication_year_y'])['cf_scxwo_y'].mean()
MNCS_y = subset_filt.groupby('Publication_year_y')['cf_scxwo_y'].mean().reset_index()
print(MNCS_y)
# Make barchart 
fig = px.bar(data_frame = MNCS_y, x="Publication_year_y", y="cf_scxwo_y", width = 600, height = 600)
#change bar colours (Visual Identity 2020)
fig.update_traces(marker_color = 'rgb(167,201,71)')
# change background colour and general font
fig.update_layout(plot_bgcolor='white', font=dict(size=18), margin=dict(r=200))
#modify x-axis to include the appropriate years (in 2020 = 2015-2018)
fig.update_xaxes(title = " ", 
    showgrid=True, 
    linecolor='black', 
    ticktext=["<b>2015</b>", "<b>2016</b>", "<b>2017</b>", "<b>2018</b>"], 
    tickvals=["2015", "2016", "2017", "2018"])
#modify y-axis to include the values of FNCS (if needed)
fig.update_yaxes(title = " ", 
    showgrid=True, 
    gridcolor="black", 
    linecolor='black', 
    ticktext=["0,0", "1,0", "2,0", "3,0"], 
    tickvals=["0.0", "1.0", "2.0", "3.0"],
    range=(0,3.01)) 
#add horizontal line 
#fig.add_hline(y=1, 
#    line_width=4, 
#    line_color='rgb(76,151,159)')
#fig.add_annotation(x=1.5, y= 1, showarrow=False, text='Världsgenomsnitt', textangle=0, xref='paper', yref="y")
# show Figure
fig.show()
