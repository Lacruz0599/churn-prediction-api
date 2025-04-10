from app.models.client_model import Client
from app.custom_types.model_method import ModelMethod


def predict_list_controller(
    method: ModelMethod,
    clients: list[Client]
): return clients


def predict_instance_controller(
    method: ModelMethod,
    client: Client
): return Client
