import numpy
import os
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from wf_ml_training import create_models
from wf_ml_prediction import perform_prediction

data = pd.read_csv("data_processed/processed_data.csv")
removable_features = ['Unnamed: 0', 'the_geom', 'cartodb_id', 'the_geom_webmercator', 'objectid', 'dispatch_date_time', 'dispatch_date', 'dispatch_time', 'hour_', 'dc_key', 'location_block', 'ucr_general', 'text_general_code', 'point_x', 'point_y']
features = list(data.columns)
features = [ft for ft in features if ft not in removable_features]

y = data["crime_code"]

X = data[features]
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.2)

create_models(train_X, train_y)

performance = [["Model", "Accuracy", "Precision", "F1-score"]]

sgd_prediction = perform_prediction(test_X, "./models/sgd_model.pkl")
performance.append(["SGD",
                   accuracy_score(test_y, sgd_prediction, normalize=True),
                   precision_score(test_y, sgd_prediction, average='micro'),
                    f1_score(test_y, sgd_prediction, average='micro')
                    ])

knn_prediction = perform_prediction(test_X, "./models/knn_model.pkl")
performance.append(["KNN",
                   accuracy_score(test_y, knn_prediction, normalize=True),
                   precision_score(test_y, knn_prediction, average='micro'),
                    f1_score(test_y, knn_prediction, average='micro')
                    ])

rf_prediction = perform_prediction(test_X, "./models/rf_model.pkl")
performance.append(["Random Forest",
                   accuracy_score(test_y, rf_prediction, normalize=True),
                   precision_score(test_y, rf_prediction, average='micro'),
                    f1_score(test_y, rf_prediction, average="micro")
                    ])

eval_dir = "./evaluation"
if not os.path.exists(eval_dir):
    os.mkdir(eval_dir)
numpy.savetxt(f'{eval_dir}/performance.txt', numpy.matrix(performance), fmt='%s')
