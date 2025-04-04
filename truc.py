import pandas as pn
import os
meteos = []


rootdir ='source_data'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(file)
        if "meteo-" in file :
            meteos.append(pn.read_csv(file))
            
print(meteos)

ulti_df = pn.DataFrame()

for elt in meteos:
    ulti_df.merge(elt)
