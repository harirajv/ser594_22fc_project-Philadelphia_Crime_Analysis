from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import os
import pickle

def create_models(X, y):
    print("Creating model with SGDClassifier")
    sgd_model = make_pipeline(StandardScaler(),SGDClassifier(max_iter=100, tol=1e-3))
    sgd_model.fit(X, y)

    print("Creating model with KNeighborsClassifier")
    knn_model = KNeighborsClassifier(n_neighbors=14)
    knn_model.fit(X, y)

    print("Creating model with RandomForestClassifier")
    rf_model = RandomForestClassifier(n_estimators=200, max_depth=32, random_state=0)
    rf_model.fit(X, y)

    outdir = './models'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    with open("models/sgd_model.pkl", "wb") as sgd_file, open("models/knn_model.pkl", "wb") as knn_file, open("models/rf_model.pkl", "wb") as rf_file:
        pickle.dump(sgd_model, sgd_file)
        pickle.dump(knn_model, knn_file)
        pickle.dump(rf_model, rf_file)
