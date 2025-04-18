
import joblib

from app.models.client_input_model import ClientInput
from app.models.client_prediction_model import ClientPrediction


model = joblib.load("app/ml_model/model_churn.pkl")


def predict_client(client: ClientInput, treshold: float):
    prediction = model.predict_proba([list(client.model_dump().values())])

    probabilty = prediction[:, 1][0]
    prediction = int(probabilty >= treshold)
    return ClientPrediction(probability=probabilty, prediction=prediction)
