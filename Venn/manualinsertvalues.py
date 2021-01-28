from matplotlib_venn import venn2, venn2_unweighted, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd
v = venn2(subsets = (32.1, 49.9, 18),
#next line would set labels outside the circles
    set_labels = ('Användare av SciLifeLab:s\nforskningsinfrastruktur   ', 'SciLifeLab:s forskare'), 
    set_colors = ('#A7C947', '#4C979F'),
#    subset_label_formatter= ("32.1%", "49.9%", "18%"),
    alpha=1.0,
    ax=plt.gca())
v.get_label_by_id("01").set_text("3415\n(50%)")
v.get_label_by_id("10").set_text(("2192\n(32%)"))
v.get_label_by_id("11").set_text(("1232\n(18%)"))
# set outer labels  
for text in v.set_labels:
    text.set_fontsize(12)
# below recolours overlapping sections to be consistent with scilifelab visual ID 
v.get_patch_by_id('11').set_color('#a48fa9')
#plt.show()
#Uncomment the above to show the figure, the below saves the figure, but a blank image will be saved if plt.show() is done first
plt.savefig("highresvenn.png", dpi=300)
