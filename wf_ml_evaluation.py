import numpy
import os
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split, TimeSeriesSplit
from wf_ml_training import create_models
from wf_ml_prediction import run_predictions, perform_prediction

data = pd.read_csv("data_processed/processed_data.csv")
removable_features = ['Unnamed: 0', 'the_geom', 'cartodb_id', 'the_geom_webmercator', 'objectid', 'dispatch_date_time',
                      'dispatch_date', 'dispatch_time', 'hour_', 'dc_key', 'location_block',
                      'text_general_code', 'point_x', 'point_y']
features = list(data.columns)
features = [ft for ft in features if ft not in removable_features]

y = data["ucr_general"]

X = data[features].drop(["ucr_general"], axis=1)

# 80% training data, 20% test data
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=0.2, shuffle=False)
training_data = pd.concat([train_X, train_y], axis=1)

training_data.to_csv("data_processed/training_data.csv")
test_X.to_csv("data_processed/testing_data.csv")

create_models(train_X, train_y)

performance = [["Model", "Accuracy", "Precision"]]

# pred = perform_prediction(test_X, "./models/knn_model_8.pkl")
# print(accuracy_score(test_y, pred, normalize=True))
# print(precision_score(test_y, pred, average='macro'))
predictions = run_predictions(test_X)
for model, pred in predictions.items():
    performance.append([
        model,
        accuracy_score(test_y, pred, normalize=True),
        precision_score(test_y, pred, average='macro')
    ])

eval_dir = "./evaluation"
if not os.path.exists(eval_dir):
    os.mkdir(eval_dir)
numpy.savetxt(f'{eval_dir}/performance.txt', numpy.matrix(performance), fmt='%s')
