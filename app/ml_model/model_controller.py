
import joblib
import pandas as pd

from app.models.client_input_model import ClientInput
from app.models.client_prediction_model import ClientPrediction


model = joblib.load("ml_model/model_churn.pkl")


def predict_client(client: ClientInput, treshold: float):

    instance = pd.DataFrame(client.model_dump(), index=[0], dtype=int)

    prediction = model.predict_proba(instance)

    probabilty = prediction[:, 1][0]
    prediction = int(probabilty >= treshold)
    return ClientPrediction(probability=probabilty, prediction=prediction)
