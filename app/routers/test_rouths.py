from fastapi import APIRouter
from typing import Annotated
from fastapi import Body


from app.custom_types.model_evaluation_metric import ModelEvaluationMetric
from app.models.client_input_model import ClientInput

router = APIRouter(
    prefix='/test-model',
    tags=['test'],
)


@router.post('/{metric}', response_model=float)
def evaluate(
    method: ModelEvaluationMetric,
    clients: Annotated[
        list[ClientInput],
        Body()]
):
    pass
