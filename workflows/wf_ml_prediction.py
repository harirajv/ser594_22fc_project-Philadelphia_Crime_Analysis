import pickle


def perform_prediction(data, model_path):
    print("Predicting with model from ", model_path)
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model.predict(data)


def run_predictions(data):
    predictions = {"knn_8": perform_prediction(data, "./models/knn_model_8.pkl"),
                   "knn_10": perform_prediction(data, "./models/knn_model_10.pkl"),
                   "knn_14": perform_prediction(data, "./models/knn_model_14.pkl"),
                   "rf": perform_prediction(data, "./models/rf_model.pkl")}
    return predictions
