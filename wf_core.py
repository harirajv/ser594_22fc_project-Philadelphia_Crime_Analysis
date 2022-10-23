from wf_dataprocessing import processing
import wf_visualization

import pandas as pd
import os

bbc_data = pd.read_csv("data_original/tweets_bbc.csv")
cnn_data = pd.read_csv("data_original/tweets_cnn.csv")
eco_data = pd.read_csv("data_original/tweets_eco.csv")
data = pd.concat([bbc_data, cnn_data, eco_data], ignore_index=True)

data = processing(data)
data.to_csv("data_processed/processed_data.csv")

summary_statistics(data)
correlation(data)
scatter_plots(data)
