from wf_dataprocessing import processing
import wf_visualization

import pandas as pd
import os

data = pd.read_csv("data_original/philly_crime_22.csv")
data = processing(data)

outdir = './data_processed'
if not os.path.exists(outdir):
    os.mkdir(outdir)
data.to_csv("data_processed/processed_data.csv")

# summary_statistics(data)
# correlation(data)
# scatter_plots(data)
