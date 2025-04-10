from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi import Body

router = APIRouter(
    prefix='/predict',
    tags=['predict'],
)


class Client(BaseModel):
    days: Annotated[int | None, Field()]
    internet_service: bool
    phone_service: bool


@router.post('/binary', response_model=list[Client])
def predict_binary_routh(clients: Annotated[list[Client], Body()]):
    pass


@router.post('/proba', response_model=list[Client])
def predict_proba_routh(clients: Annotated[list[Client], Body()]):
    pass


@router.post('/scores', response_model=list[Client])
def predict_scores_routh(clients: Annotated[list[Client], Body()]):
    pass
