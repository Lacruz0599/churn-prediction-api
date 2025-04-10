from fastapi import APIRouter
from typing import Annotated
from fastapi import Body

from app.controllers.predict_controllers import predict_instance_controller, predict_list_controller
from app.models.client_model import Client
from app.custom_types.model_method import ModelMethod

router = APIRouter(
    prefix='/predict',
    tags=['predict'],
)


@router.post('/list/{method}', response_model=list[Client])
def predict_list_routh(
    method: ModelMethod,
    clients: Annotated[
        list[Client],
        Body()]
):
    return predict_list_controller(method, clients)


@router.post('/instance/{method}', response_model=Client)
def predict_instance_routh(
    method: ModelMethod,
    client: Annotated[
        Client,
        Body()]
):
    return predict_instance_controller(method, client)
