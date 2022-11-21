from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import os
import pickle


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

    print("Creating model with RandomForestClassifier")
    rf_model = RandomForestClassifier(n_estimators=200, max_depth=32, random_state=0)
    rf_model.fit(X, y)

    outdir = './models'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    with open("models/knn_model_8.pkl", "wb") as knn_file_8,open("models/knn_model_10.pkl", "wb") as knn_file_10,open("models/knn_model_14.pkl", "wb") as knn_file_14, open("models/rf_model.pkl", "wb") as rf_file:
        pickle.dump(knn_model_8, knn_file_8)
        pickle.dump(knn_model_10, knn_file_10)
        pickle.dump(knn_model_14, knn_file_14)
        pickle.dump(rf_model, rf_file)


def create_knn_model(X, y, neighb=10):
    knn_model = KNeighborsClassifier(n_neighbors=neighb)
    knn_model.fit(X, y)

    with open(f'models/knn_model_{neighb}.pkl', "wb") as knn_file, open(
            "models/rf_model.pkl", "wb") as rf_file:
        pickle.dump(knn_model, knn_file)


def create_rf_model(X, y):
    rf_model = RandomForestClassifier(n_estimators=200, max_depth=32, random_state=0)
    rf_model.fit(X, y)

    with open("models/rf_model.pkl", "wb") as rf_file:
        pickle.dump(rf_model, rf_file)
