import pickle

def perform_prediction(data, model_path):
    print("Predicting with model from ", model_path)
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model.predict(data)


