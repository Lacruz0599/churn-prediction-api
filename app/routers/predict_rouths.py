from fastapi import APIRouter, Query, Body
from typing import Annotated

from app.controllers.predict_controllers import predict_list_controller
from app.models.client_input_model import ClientInput
from app.models.response_prediction_model import ResponsePrediction

router = APIRouter(
    prefix='/predict',
    tags=['predict'],
)


@router.post('/list', response_model=ResponsePrediction)
def predict_list_routh(
    clients: Annotated[
        list[ClientInput],
        Body(embed=True, )],

    treshold: Annotated[
        float,
        Query(
            ge=0,
            le=1,
        )] = .5,
):
    return predict_list_controller(clients, treshold)
