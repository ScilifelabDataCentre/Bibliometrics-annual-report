import pandas as pd
import plotly.express as px
##This is a mocked script. Several changes will be needed to make it fit with the 'real' data from KTH, including the files used (inc. path) and the coulm names of the dataset before manipulations are complete and a new dataset is created
#read in the data that (a) needs to have the MNCS added to it (b) contains the MNCS values 
act_pubs_fac = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /makingdraftscriptspreKTH/MNCS/mockUTfac.xlsx', sheet_name='Sheet 1', header=0, engine='openpyxl',keep_default_na=False)
act_pubs_aff = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /makingdraftscriptspreKTH/MNCS/mockUTaff.xlsx', sheet_name='Sheet 1', header=0, engine='openpyxl',keep_default_na=False)
act_pubs = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /makingdraftscriptspreKTH/MNCS/mockUT.xlsx', sheet_name='Sheet 1', header=0, engine='openpyxl',keep_default_na=False)
exp_pubs = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /makingdraftscriptspreKTH/MNCS/expected_cit.xlsx', sheet_name='Sheet 1', header =0, engine='openpyxl',keep_default_na=False)
#need to filter dataframes to include only the years to be included this time (2020 is 2015-2018). UNCOMMENT THIS
########act_pubs_ar = act_pubs[(act_pubs['Doc_type_code_rev'] == 'RV') | (act_pubs['Doc_type_code_rev'] == 'AR')]
########exp_pubs_ar = exp_pubs[(exp_pubs['Doc_type_code_rev'] == 'RV') | (exp_pubs['Doc_type_code_rev'] == 'AR')]
act_pubs_filt = act_pubs[(act_pubs['Year'] > 2014) & (act_pubs['Year'] < 2019)]
act_pubs_filt_fac = act_pubs_fac[(act_pubs['Year'] > 2014) & (act_pubs_fac['Year'] < 2019)]
act_pubs_filt_aff = act_pubs_aff[(act_pubs['Year'] > 2014) & (act_pubs_aff['Year'] < 2019)]
exp_pubs_filt = exp_pubs[(exp_pubs['Year'] > 2014) & (exp_pubs['Year'] < 2019)]
#merge the two files (actual on left), this will join the MNCS value to each year and field combo
#need to modify columns, only need on= and col names if col names shared. However, need left_on=[] and right_on=[] with 'df_col' if the column names differ  
#FILER APPLIED BELOW- UNCOMMMENT! 
mergeddf = pd.merge(act_pubs_filt, exp_pubs_filt, how='left', on=['Year','Field'])
mergeddf_fac = pd.merge(act_pubs_filt_fac, exp_pubs_filt, how='left', on=['Year','Field'])
mergeddf_aff = pd.merge(act_pubs_filt_aff, exp_pubs_filt, how='left', on=['Year','Field'])
#create a column that shows mean normalised citation score (MNCS) for each 
mergeddf['MNCS'] = mergeddf['Citations']/mergeddf['expect_cit']
mergeddf_aff['MNCS'] = mergeddf_aff['Citations']/mergeddf_aff['expect_cit']
mergeddf_fac['MNCS'] = mergeddf_fac['Citations']/mergeddf_fac['expect_cit']
#to get the MNCS for each field and year, need to sum those in same field and year and divide by the total number citations in that group
MNCS_f_fell = mergeddf.groupby(['Field']).apply(lambda x:x['MNCS'].sum()/len(x)).reset_index(name='MNCS_df')
MNCS_f_fell.insert(2, 'Source', 'Fellow')
MNCS_f_aff = mergeddf_aff.groupby(['Field']).apply(lambda x:x['MNCS'].sum()/len(x)).reset_index(name='MNCS_df')
MNCS_f_aff.insert(2, 'Source', 'Affil')
MNCS_f_fac = mergeddf_fac.groupby(['Field']).apply(lambda x:x['MNCS'].sum()/len(x)).reset_index(name='MNCS_df')
MNCS_f_fac.insert(2, 'Source', 'Facs')
#ensure that there are not blank rows around in your files, as these will remain with concatenate (shouldnt be an issue with the filters applied though)
together=pd.concat([MNCS_f_fell, MNCS_f_aff, MNCS_f_fac])
#To change field categories to Swedish
####d = {'cat1':'Swed1', 'cat2':'Swed2','cat3':'Swed3'.......}
####together = together.replace(d)
#generate a barchart, with bars coloured by field (colours correspond to visual ID), order bars such that 'total' (i.e. overall MNCS for the year) is first 
fig = px.bar(together, x="Field", y="MNCS_df", 
    color='Source', 
    color_discrete_sequence=['#045C64', '#A6A6A6', '#A7C947'])
#, '#491F53','#D3E4A3' 
#set the order of categories 
#update figure layout to showed a grouped barchart, white background, sert font size and set overall size
fig.update_layout(barmode='group', 
    plot_bgcolor='white', 
    font=dict(size=14), 
    margin=dict(r=110, l=10), 
    autosize =False, 
    width = 1100, height = 600,
    legend_title_text='Legend Name')
#modify x-axis
fig.update_xaxes(title = " ", 
    showgrid=True, 
    linecolor='black') 
#Modify text and values to reflect appropriate range (can do all years, or just consistent with leiden. For 2020 = 2015-2018)
##    ticktext=["<b>2015</b>", "<b>2016</b>", "<b>2017</b>", "<b>2018</b>"],
##    tickvals=["2015", "2016", "2017", "2018"])
#modify y-axis
fig.update_yaxes(title = " ", 
    showgrid=True, 
    gridcolor="black", 
    linecolor='black', 
#as it is a Swedish report, decimal places must be presented as e.g. 1,5 not 1.5 
    ticktext=["0,0", "0,5", "1,0", "1,5", "2,0"],
    tickvals=["0", "0.5", "1.0", "1.5", "2.0"],
#change range to envelope the appropriate range (MNCS should be within 2, so this should be fine)
    range=[0,2])
##fig.update_traces(marker_line_width=0)
#put in the line on the graph for average 
fig.add_annotation(x=1.138, y= 1, showarrow=False, text='Världsgenomsnitt', textangle=0, xref='paper', yref="y")
fig.add_shape(type="line", x0=0, x1 ='1', xref='paper', y0=1, y1=1, line=dict(color='#4C979F', width=4))
fig.show()