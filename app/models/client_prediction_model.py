
from dataclasses import Field
from typing import Annotated
from pydantic import BaseModel, Field


class ClientPrediction(BaseModel):
    prediction: Annotated[int | None, Field()]
    probability: Annotated[float | None, Field()]
