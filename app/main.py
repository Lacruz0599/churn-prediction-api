from fastapi import FastAPI

from app.routers import predict_rouths

app = FastAPI()

app.include_router(
    predict_rouths.router,
    prefix='/churn-api/v1')
