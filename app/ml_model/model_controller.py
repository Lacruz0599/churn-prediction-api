

from app.models.client_input_model import ClientInput


class ModelX():

    def predict(x):
        return [1, 1, 1, 1, 1, 1, 1, 1]

    def predict_proba(x):
        return [1, 1, 1, 1, 1, 1, 1, 1]

    def score(x, y):
        return .1


model = ModelX()


def model_predict_list(clients: list[ClientInput]):

    for client in clients:
        client.model_dump.values


def model_predict_instance(client: ClientInput):
    return
