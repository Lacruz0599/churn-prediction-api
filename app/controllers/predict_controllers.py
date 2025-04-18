from app.ml_model.model_controller import predict_client
from app.models.client_input_model import ClientInput
from app.models.client_prediction_model import ClientPrediction
from app.models.response_prediction_model import ResponsePrediction


def predict_list_controller(
    clients: list[ClientInput],
    treshold: float
):
    predictions = []
    for client in clients:
        prediction = predict_client(client, treshold)
        predictions.append(prediction)

        response = ResponsePrediction(predictions=predictions)
    return response
