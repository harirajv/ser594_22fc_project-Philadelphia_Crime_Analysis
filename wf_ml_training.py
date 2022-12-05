from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.neighbors import KNeighborsClassifier
import os
import pickle


def create_best_model(X, y):

    model = RandomForestClassifier()
    param_search = {
        'n_estimators': [50, 100, 200, 400],
        'max_features': ['sqrt', 'log2'],
        'max_depth': [4, 8, 16, 32, 64]
    }
    tscv = TimeSeriesSplit(n_splits=4)
    gsearch = GridSearchCV(estimator=model, cv=tscv, param_grid=param_search, scoring='accuracy')
    gsearch.fit(X, y)
    best_model = gsearch.best_estimator_
    best_parameters = gsearch.best_params_
    print(f"Best parameters for {model}: ", best_parameters)
    return best_model

def create_models(X, y):
    print("Creating model with KNeighborsClassifier with 8 neighbors")
    knn_model_8 = KNeighborsClassifier(n_neighbors=8)
    knn_model_8.fit(X, y)

    print("Creating model with KNeighborsClassifier with 10 neighbors")
    knn_model_10 = KNeighborsClassifier(n_neighbors=10)
    knn_model_10.fit(X, y)

    print("Creating model with KNeighborsClassifier with 14 neighbors")
    knn_model_14 = KNeighborsClassifier(n_neighbors=14)
    knn_model_14.fit(X, y)

    print("Grid search for best parameters of RandomForestClassifier")
    rf_best_model = create_best_model(X, y)

    outdir = './models'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    with open("models/knn_model_8.pkl", "wb") as knn_file_8,\
            open("models/knn_model_10.pkl", "wb") as knn_file_10,\
            open("models/knn_model_14.pkl", "wb") as knn_file_14,\
            open("models/rf_best_model.pkl", "wb") as rf_best_file:
        pickle.dump(knn_model_8, knn_file_8)
        pickle.dump(knn_model_10, knn_file_10)
        pickle.dump(knn_model_14, knn_file_14)
        pickle.dump(rf_best_model, rf_best_file)
