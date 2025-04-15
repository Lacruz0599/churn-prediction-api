from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import predict_rouths

app = FastAPI()


# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    predict_rouths.router,
    prefix='/churn-api/v1')
