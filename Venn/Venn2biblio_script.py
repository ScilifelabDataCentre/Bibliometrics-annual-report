from matplotlib_venn import venn2, venn2_unweighted, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd
# This script makes a simple 2 group venn diagram
# it automatically calculates percentages and values and labels accordingly, just put in correct data 
# put data for 2 groups 
facilitiesdf = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /FinalKTHdata/Stitcheddata/Facilities_reportingexclusive.xlsx', sheet_name='Sheet1', engine='openpyxl')
affiliatesdf = pd.read_excel('/Users/liahu895/Documents/scilifelab/Annual report /FinalKTHdata/Stitcheddata/affiliates_JIF_statsinc.xlsx', sheet_name='Sheet1', engine='openpyxl')
lastfivefacs = facilitiesdf[(facilitiesdf['Publication_year_y'] > 2014) & (facilitiesdf['Publication_year_y'] < 2021)]
lastfiveaffs = affiliatesdf[(affiliatesdf['Publication_year_y'] > 2014) & (affiliatesdf['Publication_year_y'] < 2021)]
facsrevsarts = lastfivefacs[(lastfivefacs['Doc_type_code_rev_y'] == 'rv') | (lastfivefacs['Doc_type_code_rev_y'] == 'ar')]
affsrevsarts = lastfiveaffs[(lastfiveaffs['Doc_type_code_rev_y'] == 'RV') | (lastfiveaffs['Doc_type_code_rev_y'] == 'AR')]
fac_set_UT = set(facsrevsarts["UT"])
aff_set_UT = set(affsrevsarts["UT"])
# Make a weighted Venn
total = len(fac_set_UT.union(aff_set_UT))
v = venn2(subsets = [fac_set_UT, aff_set_UT],
#next line would set labels outside the circles
    set_labels = ('Användare av SciLifeLab:s\nforskningsinfrastruktur   ', 'SciLifeLabs forskare'), 
    set_colors = ('#A7C947', '#4C979F'),
    subset_label_formatter=lambda x: f"\n({(x/total):1.0%})",
    alpha=1.0,
    ax=plt.gca())
# set outer labels  
for text in v.set_labels:
    text.set_fontsize(12)
# below recolours overlapping sections to be consistent with scilifelab visual ID 
v.get_patch_by_id('11').set_color('#a48fa9')
plt.show()
#to save the figure are a high res figure, uncomment the below. 
# Note though that a blank image will be saved if plt.show() is done first, so comment that out first 
plt.savefig("highresvenn.png", dpi=300)
