from wf_dataprocessing import processing
from wf_visualization import summary_statistics, correlation, draw_plots

import pandas as pd
import os

data_20 = pd.read_csv("data_original/philly_crime_20.csv")
data_21 = pd.read_csv("data_original/philly_crime_21.csv")
data_22 = pd.read_csv("data_original/philly_crime_22.csv")
data = pd.concat([data_20, data_21, data_22], axis=0)
data = processing(data)

outdir = './data_processed'
if not os.path.exists(outdir):
    os.mkdir(outdir)
data.to_csv("data_processed/processed_data.csv")

data = pd.read_csv("data_processed/processed_data.csv")

summary_statistics(data)
correlation(data)
draw_plots(data)
