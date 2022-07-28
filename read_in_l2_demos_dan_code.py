

# This is a script to read in the demographics file from L2. Big boy.

import pandas as pd
import os

# Set root directory (working in Downloads for now; should move eventually)
root = 'C:/Users/Igor/Downloads'
orig_fname = root + 'VM2--CA--2022-07-01-DEMOGRAPHIC.tab'
new_fname = root + 'VM2--CA--2022-07-01-DEMOGRAPHIC-subset.tab' ## can I make this .csv right away? ## also maybe make .dta for DF.

# baby_subset = str(row[0:5]) + str(row[6:10])
# subset = str(row[0:44]) + str(row[47:50]) + str(row[55:58]) + str(row[62:65]) + str(row[67:85]) + str(row[87:123]) + '\n'

# pick out a few LALVOTERIDs that were in the vote history file.
rows = 1
with open(new_fname_sample_ids, 'w') as new_file:
    with open(orig_fname, 'r') as orig_file:
        for row in orig_file:
            lalvoterid = int(row[0]) ## make sure this points to the actual LALVOTERID
            if lalvoterid.isin(["LALCA516105812", "LALCA22129469"]): ## REPLACE REPLACE REPLACE
                subset = str(row[0:5]) ## not sure I fully understand doing this here, but also up there
                bytes = new_file.write(subset) ## see note about subset above
                rows = rows + 1
                if (rows % 100000)==0: ## took off a zero assuming this is something like chunks...
                    print(int(rows/100000))


####################

# Pick out men age 19-29 from the 1870 to 1940 censuses
# rows = 1
# with open(new_fname_young_men, 'w') as new_file:
# 	with open(orig_fname, 'r') as orig_file:
# 		for row in orig_file:
# 			age = int(row[40:43])
# 			sex = int(row[39:40])
# 			if sex==1 and age>=19 and age<=29:
# 				subset = str(row[0:126]) + '\n'
# 				bytes = new_file.write(subset)
# 				rows = rows + 1
# 				if (rows % 1000000)==0:
# 					print(int(rows/1000000))

