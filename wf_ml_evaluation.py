import numpy
import os
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split, TimeSeriesSplit
from wf_ml_training import create_models
from wf_ml_prediction import run_predictions, perform_prediction

data = pd.read_csv("data_processed/processed_data.csv")

features = ['dc_dist_1', 'dc_dist_2', 'dc_dist_3', 'dc_dist_5',
       'dc_dist_6', 'dc_dist_7', 'dc_dist_8', 'dc_dist_9', 'dc_dist_12',
       'dc_dist_14', 'dc_dist_15', 'dc_dist_16', 'dc_dist_17', 'dc_dist_18',
       'dc_dist_19', 'dc_dist_22', 'dc_dist_24', 'dc_dist_25', 'dc_dist_26',
       'dc_dist_35', 'dc_dist_39', 'dc_dist_77', 'psa_1', 'psa_2', 'psa_3',
       'psa_4', 'psa_A', 'psa_Unknown', 'dispatch_day_name_Friday',
       'dispatch_day_name_Monday', 'dispatch_day_name_Saturday',
       'dispatch_day_name_Sunday', 'dispatch_day_name_Thursday',
       'dispatch_day_name_Tuesday', 'dispatch_day_name_Wednesday', 'lat', 'lng',
       'dispatch_day', 'dispatch_month', 'dispatch_year', 'dispatch_time_seconds',
       'dispatch_hour', 'dispatch_minute', 'dispatch_second']
target = 'ucr_general'

tscv = TimeSeriesSplit()
train_splits = []
test_splits = []

for train_index, test_index in tscv.split(data):
    X_train, X_test = data.iloc[train_index,:], data.iloc[test_index,:]
    train_splits.append(X_train)
    test_splits.append(X_test)

train_data = pd.concat(train_splits)
test_data = pd.concat(test_splits)

print("Train data shape: ", train_data.shape)
print("Test data shape: ", test_data.shape)

train_X = train_data.drop(['ucr_general'], axis = 1)[features]
train_y = train_data['ucr_general']

training_data = pd.concat([train_X, train_y], axis=1)

training_data.to_csv("data_processed/training_data.csv")

test_X = test_data.drop(['ucr_general'], axis = 1)[features]
test_y = test_data['ucr_general']
test_X.to_csv("data_processed/testing_data.csv")

create_models(train_X, train_y)

performance = [["Model", "Accuracy", "Precision"]]

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
