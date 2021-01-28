import pandas as pd
import numpy as np
import plotly.express as px
##This is a mocked script. Several changes will be needed to make it fit with the 'real' data from KTH, including the files used (inc. path) and the coulm names of the dataset before manipulations are complete and a new dataset is created
#read in the data that (a) represents 'raw' data abstract (b) represents the threshold values  
pp_thresh = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /makingdraftscriptspreKTH/PP(top10)/pp_thresh_vals.xlsx', sheet_name='Sheet 1', header=0, engine='openpyxl',keep_default_na=False)
mock_data = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /makingdraftscriptspreKTH/PP(top10)/mock_UT_pp.xlsx', sheet_name='Sheet 1', header =0, engine='openpyxl',keep_default_na=False)
#need to filter dataframes to include only the years to be included this time (2020 is 2015-2018) and filter data to include only articles and reviews. UNCOMMENT THIS
########mock_data_ar = mock_data[(mock_data['Doc_type_code_rev'] == 'RV') | (mock_data['Doc_type_code_rev'] == 'AR')]
########Modify below to account for above filter as needed
pp_thresh_filt = pp_thresh[(pp_thresh['Year'] > 2014) & (pp_thresh['Year'] < 2019)]
mock_data_filt = mock_data[(mock_data['Year'] > 2014) & (mock_data['Year'] < 2019)]
# To calculate pp(top10), need to know the proportion of papers cited > threshold for top 10% most cited
mergeddf = pd.merge(mock_data_filt, pp_thresh_filt, how='left', on=['Year','Field']) 
# merge the two files (data on left), put the two together 
#create a column that shows whether the number of citations gained exceeded the top 10% threshold
mergeddf['PPtopten'] = np.where(mergeddf['Citations']>=mergeddf['PPthresh'], 1, 0)
# you then need to sum the number you just generated to get a count of the number of papers that are in the top10% most cited
pptopten_yf = mergeddf.groupby(['Year','Field']).apply(lambda x:x['PPtopten'].sum()/len(x)).reset_index(name='PPtopten')
pptopten_yf['PPtopten'] = pptopten_yf['PPtopten'].multiply(100)
# calculate overall values for each year (comparable to Leiden)
pptopten_y = mergeddf.groupby(['Year']).apply(lambda x:x['PPtopten'].sum()/len(x)).reset_index(name='PPtopten')
pptopten_y['PPtopten'] = pptopten_y['PPtopten'].multiply(100)
pptopten_y.insert(1, 'Field', 'Overall')
#print(pptopten_y.head())
# add the overall values for the years to the dataframe containing the values calculated for each field in each year
#ensure that there are not blank rows around in your files, as these will remain with concatenate (shouldnt be an issue with the filters applied though)
concattopten=pd.concat([pptopten_y, pptopten_yf])
concattopten.Year = pd.Categorical(concattopten.Year)
#To change field categories to Swedish
####d = {'cat1':'Swed1', 'cat2':'Swed2','cat3':'Swed3'.......}
####concattopten = concattopten.replace(d)
#generate a barchart, with bars coloured by field (colours correspond to visual ID), order bars such that 'total' (i.e. overall MNCS for the year) is first 
fig = px.bar(concattopten, x="Field", y="PPtopten", 
    color='Year', 
    color_discrete_sequence=['#045C64', '#A6A6A6', '#A7C947', '#491F53','#D3E4A3'])
#set the order of categories 
#    category_orders={"Field":["Overall", "Bacteria", "Genetics", "Protist", "Virus"]})
#update figure layout to showed a grouped barchart, white background, sert font size and set overall size
fig.update_layout(barmode='group', 
    plot_bgcolor='white', 
    font=dict(size=14), 
    margin=dict(r=150, l=10), 
    autosize =False, 
    width = 1100, height = 600,
    legend_title_text='        <b>År</b>')
#modify x-axis
fig.update_xaxes(title = " ", 
    showgrid=True, 
    linecolor='black',)
#Modify text and values as needed
#    ticktext=["<b>2015</b>", "<b>2016</b>", "<b>2017</b>", "<b>2018</b>"],
#    tickvals=["Overall", "Bacteria", "Genetics", "Protist", "Virus"]
#modify y-axis
fig.update_yaxes(title = " ", 
    showgrid=True, 
    gridcolor="black", 
    linecolor='black', 
#as it is a Swedish report, decimal places must be presented as e.g. 1,5 not 1.5 
    ticktext=["0", "25", "50", "75", "100"],
    tickvals=["0", "25", "50", "75", "100"],
#change range to envelope the appropriate range (MNCS should be within 2, so this should be fine)
    range=[0,105])
fig.update_traces(marker_line_width=0)
#put in the line on the graph for average 
fig.add_annotation(x=1.15, y= 10, showarrow=False, text='Världsgenomsnitt', textangle=0, xref='paper', yref="y")
fig.add_shape(type="line", x0=0, x1='1', xref='paper', y0=10, y1=10, line=dict(color='#4C979F', width=4))
fig.show()