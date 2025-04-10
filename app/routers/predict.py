from fastapi import APIRouter
from typing import Annotated
from fastapi import Body

from app.models.client_model import Client

router = APIRouter(
    prefix='/predict',
    tags=['predict'],
)


@router.post('/binary', response_model=list[Client])
def predict_binary_routh(clients: Annotated[list[Client], Body()]):
    pass


@router.post('/proba', response_model=list[Client])
def predict_proba_routh(clients: Annotated[list[Client], Body()]):
    pass


@router.post('/scores', response_model=list[Client])
def predict_scores_routh(clients: Annotated[list[Client], Body()]):
    pass
