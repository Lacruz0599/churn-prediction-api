from app.models.client_input_model import ClientInput
from app.models.client_prediction_model import ClientPrediction
from app.models.response_prediction_model import ResponsePrediction


def predict_list_controller(
    clients: list[ClientInput],
    treshold: float
):
    predictions = []
    for client in clients:
        prediction = ClientPrediction(prediction=1, probability=.5)
        predictions.append(prediction)

        response = ResponsePrediction(predictions=predictions)
    return response
