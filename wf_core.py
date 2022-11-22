from wf_dataprocessing import processing
from wf_visualization import summary_statistics, correlation, draw_plots

import pandas as pd
import os

data = pd.read_csv("data_original/philly_crime_22.csv")
data = processing(data)

outdir = './data_processed'
if not os.path.exists(outdir):
    os.mkdir(outdir)
data.to_csv("data_processed/processed_data.csv")

summary_statistics(data)
correlation(data)
draw_plots(data)
