
from dataclasses import Field
from typing import Annotated
from pydantic import BaseModel, Field


class ClientPrediction(BaseModel):
    prediction: int
    probability: float
