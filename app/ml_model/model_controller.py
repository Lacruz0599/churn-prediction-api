

from app.models.client_input_model import ClientInput
from app.models.client_prediction_model import ClientPrediction


class ModelX():

    def predict(x):
        return [1]

    def predict_proba(x):
        return [.5]

    def score(x, y):
        return .1


model = ModelX()


def predict_client(client: ClientInput, treshold: float):
    prediction = model.predict_proba(client)

    probabilty = prediction[0][1]
    prediction = int(probabilty >= treshold)
    return ClientPrediction(probability=probabilty, prediction=prediction)
