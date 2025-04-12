from fastapi import APIRouter, Query, Body
from typing import Annotated

from app.controllers.predict_controllers import predict_instance_controller, predict_list_controller
from app.models.client_input_model import ClientInput
from app.models.client_prediction_model import ClientPrediction
from app.custom_types.model_method import ModelMethod
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
        Query()] = .5,
):
    return predict_list_controller(clients, treshold)


@router.post('/instance/{method}', response_model=ClientPrediction)
def predict_instance_routh(
    method: ModelMethod,
    client: Annotated[
        ClientInput,
        Body()]
):
    return predict_instance_controller(method, client)
