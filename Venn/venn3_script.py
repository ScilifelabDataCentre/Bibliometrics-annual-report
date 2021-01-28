from matplotlib_venn import venn3, venn3_unweighted, venn3_circles
import matplotlib.pyplot as plt
# This script will enable you to make a simple 3 group venn
# put data for 2 groups 
ssthree = {'100':30, '010':30, '110':17, '001':30, '101':17, '011':17, '111':5} 
# Make a weighted Venn
v3 = venn3(subsets = ssthree,
#next line would set labels outside the circles
    set_labels = ('', '', ''),
#'Affiliated   \nResearchers', 'Facility\n Users', 'Fellows' 
    set_colors = ('#a7c947', '#045c64', '#491F53'),
    ax=plt.gca())
v3.get_label_by_id('100').set_text('Affiliated'+"\n"+'Researchers'+"\n"+"\n"+'30%')
# add this to get labels inside 'Affiliated'+"\n"+'Researchers'+"\n"+"\n"+
v3.get_label_by_id('100').set_x(-0.35)
v3.get_label_by_id('100').set_y(+0.2)
v3.get_label_by_id('010').set_text('Facility'+"\n"+'Users'+"\n"+"\n"+'30%')
#  add this to get labels inside'Facility'+"\n"+'Users'+"\n"+"\n"+
v3.get_label_by_id('010').set_x(0.35)
v3.get_label_by_id('010').set_y(+0.2)
v3.get_label_by_id('110').set_text('17%')
v3.get_label_by_id('001').set_text('Fellows'+"\n"+"\n"+'30%')
# add this to get labels inside 'Fellows'+"\n"+"\n"+
v3.get_label_by_id('001').set_y(-0.4)
v3.get_label_by_id('101').set_text('17%')
v3.get_label_by_id('011').set_text('17%')
v3.get_label_by_id('111').set_text('5%')
for text in v3.set_labels:
    text.set_fontsize(12)
# below recolours overlapping sections to be consistent with scilifelab visual ID 
v3.get_patch_by_id('111').set_color('#4c979f')
v3.get_patch_by_id('011').set_color('#d3e4a3')
v3.get_patch_by_id('110').set_color('#a48fa9')
v3.get_patch_by_id('101').set_color('#d2e5e7')
#add outer edge lines to the weighed venn 
venn3_circles(subsets = ssthree)
plt.show()
# now make unweighted 3 circle venn 
#l3 = venn3_unweighted(subsets = ssthree,
#   set_labels = ('Affiliated   \nResearchers', 'Facility\n Users', 'Fellows'),
#   set_colors = ('#a7c947', '#045c64', '#491F53'),
#    ax=plt.gca())
#l3.get_label_by_id('100').set_text('30%')
# add this to get labels inside 'Affiliated'+"\n"+'Researchers'+"\n"+"\n"+
#l3.get_label_by_id('100').set_x(-0.4)
#l3.get_label_by_id('100').set_y(+0.2)
#l3.get_label_by_id('010').set_text('30%')
#  add this to get labels inside'Facility'+"\n"+'Users'+"\n"+"\n"+
#l3.get_label_by_id('010').set_x(0.4)
#l3.get_label_by_id('010').set_y(+0.2)
#l3.get_label_by_id('110').set_text('17%')
#l3.get_label_by_id('001').set_text('30%')
# add this to get labels inside 'Fellows'+"\n"+"\n"+
#l3.get_label_by_id('001').set_y(-0.45)
#l3.get_label_by_id('101').set_text('17%')
#l3.get_label_by_id('011').set_text('17%')
#l3.get_label_by_id('111').set_text('5%')
#for text in l3.set_labels:
#    text.set_fontsize(12)
#plt.show()