# Bibliometrics-annual-report
This repository holds the python scripts to create the bibliometrics analysis completed for the annual report 2020 

There are 4 main types of code to be considered here:

1) Scripts within JIF involve looking at publication numbers for a given group over time. These scripts deal with aligning JIF scores to publications and producing barcharts to show the number of publications produced in each year. 
2) Scripts within Venn look at overlaps in the number of publications between groups. 
3) Scripts within MNCStest consider the calculation of the mean normalised citation scores. The scripts enable the calculation of the MNCS as well as produce the associated graphs.  
4) Scripts within PPtopten consder the calculation of the percentage of publications in the top 10% most cited (PP(top10)). The scripts enable the calculation of the PP(top10) as well as produce the associated graphs. 

############################
  JIF scripts descriptions
############################

JIFbove9 - used to produce graphs that considered how many publications had a JIF higher than 9 (i.e. a high JIF)

JIFmapping - for mapping JIF to publications 

rawnumbersgraph - considers files using the raw number of publications (with JIF already matched - use files produced from JIF mapping)


#############################
  Venn scripts descriptions 
#############################

Venn2biblio_script - this creates a 2 bubble weighted venn diagram in which sets are created from raw data and values are automatically calculated. Requirements of the VI and format are met. 300 dpi resolution is set during the save and is sufficient for print quality.  

Venn3_script - this was not used for the report, but could be used to generate a 3 bubble weighted venn diagram, if one was ever needed. Adjustts would be needed to align with the format requirements. See Venn2biblio_script for the colours and text used. It was recommended that bright colours were used, with no outline on bubbles. Had to maintain the contrasts in the colours though, so that the bubble edges stay clear. 

manualinsertvalues - this script has all the format settings of Venn2biblio_script. The primary difference here is that values can be manually inserted. Thus, if calculations are completed elsewhere, those values can be inserted into this script to generate a 2 bubble venn diagram that reflects those values. 

#############################
  MNCS scripts descriptions 
#############################

Correctedforyear - this script calculates the MNCS per year 

replicateJRmock - an experimental script that could be used to group MNCS by field and year 

fieldinx - another experimental script that shows much the same as replicateJRmock, but with the graph rearranged so that the fields, rather than year, are on the x-axis

#################################
  PPtopten scripts descriptions 
#################################

PPtoptenforyear - this script uses the files provided by KTH to calculate the PP(top10) scores for each year. It's the average score of the pptop10 values calculated by KTH for each publication within a given year. 

pptest - this script was created to calculate PP(top10) assuming you had no direct calculations from KTH, but did have scores for a field. The graph within this script does deal with fields on the x-axis, rather than years (as seen in annual reports and PPtoptenforeyear above). This part of the script could be useful when calculations can be made across fields rather than overall scores for the years).  


########################################
NOTE ABOUT PRODUCTION OF FILES FOR PRINT 
########################################

Matplotlib (used for the venn diagram) can have settings adjusted such that files are generated with 300dpi. This was found to be sufficient resolution for print in the report. The resolution of images produced by plotly can be altered by changing the size of the image (1500 x 1500 pixels is sufficient - axis text must be adjusted accordingly in this case), or by using a package called kaleido when saving images and setting resolution there. 
