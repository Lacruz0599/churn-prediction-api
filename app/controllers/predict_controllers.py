

from enum import Enum
from app.models.client_model import Client


class ModelMethod(str, Enum):
    binary = 'binary'
    proba = 'proba'
    scores = 'scores'


def predict_list_controller(
    method: ModelMethod,
    clients: list[Client]
): pass


def predict_instance_controller(
    method: ModelMethod,
    client: Client
): pass
