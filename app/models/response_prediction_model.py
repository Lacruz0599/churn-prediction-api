
from pydantic import BaseModel

from app.models.client_prediction_model import ClientPrediction


class ResponsePrediction(BaseModel):
    predictions: list[ClientPrediction]
